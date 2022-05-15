from PyQt5.QtWidgets import *
from kayit import kayitUI
from giris import girisUI
from baslangic import baslangicUI
from uygulama import uygulamaUI
from veritabani import *
import sys

userMail = ""

class baslangic(QMainWindow, baslangicUI):

    def __init__(self):
        super(baslangic, self).__init__()

        self.setupUi(self)

        self.pushButton.clicked.connect(self.kayit)
        self.pushButton_2.clicked.connect(self.giris)

    def giris(self):
        girisWindow = giris()
        widget.addWidget(girisWindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def kayit(self):
        kayitWindow = kayit()
        widget.addWidget(kayitWindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class kayit(QMainWindow, kayitUI):

    def __init__(self):
        super(kayit, self).__init__()

        self.setupUi(self)

        self.pushButton.clicked.connect(self.kayit_ol)

    def kayit_ol(self):
        isim = self.textEdit.toPlainText()
        soyisim = self.textEdit_2.toPlainText()
        email = self.textEdit_3.toPlainText()
        pasword = self.textEdit_4.toPlainText()
        rvm = False
        rezervasyonlar = ""

        search = search_user(email)

        if search != None:
            print('Böyle bir kullanıcı var')



        else:
            insert(isim, soyisim, email, pasword, rvm, rezervasyonlar)
            print('kayıt başarılı')
            self.ekranGecis()

    def ekranGecis(self):
        girisWindow = giris()
        widget.addWidget(girisWindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)



class giris(QMainWindow, girisUI):


    def __init__(self):
        super(giris, self).__init__()

        self.setupUi(self)

        self.pushButton.clicked.connect(self.giris_yap)

        self.password = ""
        self.email = ""


    def giris_yap(self):
        global userMail
        self.email = self.textEdit.toPlainText()
        self.password = self.textEdit_2.toPlainText()

        search = search_user(self.email)

        if search == None:
            print('Böyle bir kullanıcı yok')

        elif self.password == search[4]:
            print('Başarılı giriş')
            userMail = self.email
            self.ekranGecis()

        else:
            print('Şifre yanlış')


    def ekranGecis(self):
        uygulamaWindow = uygulama()
        widget.addWidget(uygulamaWindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(800)


class uygulama(QMainWindow, uygulamaUI):

    def __init__(self):
        self.email = userMail

        user = search_user(self.email)
        self.ad = user[1]
        self.rezervasyon = user[6]

        super(uygulama, self).__init__()

        self.setupUi(self)

        # Tab 1
        self.label.setText(f'Hoşgeldin {self.ad}')
        self.pushButton_.clicked.connect(self.rezervasyon_yap)

        # Tab 2
        self.pushButton_2.clicked.connect(self.iptal_et)
        self.rezervasyon_goruntule()



        # Tab 3
        self.pushButton_3.clicked.connect(self.email_degistir)
        self.pushButton_4.clicked.connect(self.sifre_degistir)
        self.pushButton_5.clicked.connect(self.sil)


    def rezervasyon_yap(self):
        gun = self.dateEdit.text()
        kisi = self.lineEdit.text()

        self.rezervasyon += f"{gun} {kisi} "

        rezervasyonlar(self.email, self.rezervasyon)

        self.rezervasyon_goruntule()


    def rezervasyon_goruntule(self):
        if self.rezervasyon != "":
            self.rezervasyon_yazı = ""
            liste = self.rezervasyon.split()
            for i in range(len(liste)):
                if i % 2 == 0:
                    self.rezervasyon_yazı += f"Gün: {liste[i]}    "

                else:
                    self.rezervasyon_yazı += f"Kişi: {liste[i]}\n"

            self.label_4.setText(self.rezervasyon_yazı)

        else:
            self.label_4.setText('Rezervasyonunuz bulunmamaktadır')



    def iptal_et(self):
        gun = self.dateEdit_2.text()
        liste = self.rezervasyon.split()
        if gun in liste:
            a = liste.index(gun)
            liste.pop(a)
            liste.pop(a)
            self.rezervasyon = ""
            for i in range(len(liste)):
                self.rezervasyon += liste[i] + " "
            self.rezervasyon_goruntule()
            rezervasyonlar(self.email, self.rezervasyon)
        else:
            self.label_6.setText("Böyle bir rezervasyon bulunmamaktadır")





    def email_degistir(self):
        newEmail = self.lineEdit_2.text()
        update_email(self.email, newEmail)
        self.lineEdit_2.clear()

    def sifre_degistir(self):
        newPasword = self.lineEdit_3.text()
        update_password(self.email, newPasword)
        self.lineEdit_3.clear()

    def sil(self):
        delete_account(self.email)
        baslangicWindow = baslangic()
        widget.addWidget(baslangicWindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(612)







create_table()
app = QApplication(sys.argv)
baslangicWindow = baslangic()
widget = QStackedWidget()
widget.addWidget(baslangicWindow)
widget.show()
widget.setWindowTitle('Otel Otomasyonu')
widget.setFixedWidth(612)
widget.setFixedHeight(633)
app.exec_()

