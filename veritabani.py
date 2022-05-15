import sqlite3 as sql

def create_table():
    conn = sql.connect('proje.db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS USERS(
        id integer PRIMARY KEY,
        name text,
        lastname text,
        email text,
        password text,
        rvm Bool,
        rezervasyonlar text
    ) """)

    conn.commit()
    conn.close()

def insert(name, lastname, email, password, rvm, rezervasyonlar):
    conn = sql.connect('proje.db')
    cursor = conn.cursor()

    add_command = """INSERT INTO USERS(name, lastname, email, password, rvm, rezervasyonlar) VALUES {} """
    data = (name, lastname, email, password, rvm, rezervasyonlar)

    cursor.execute(add_command.format(data))

    conn.commit()
    conn.close()

def search_user(email):
    conn = sql.connect('proje.db')
    cursor = conn.cursor()

    search_command = """SELECT * from USERS WHERE email = '{}' """
    cursor.execute(search_command.format(email))

    user = cursor.fetchone()

    conn.close()
    return user

def update_password(email, newPassword):
    conn = sql.connect('proje.db')
    cursor = conn.cursor()

    upd_command = """UPDATE USERS SET password = '{}' WHERE email = '{}' """
    cursor.execute(upd_command.format(newPassword, email))

    conn.commit()
    conn.close()

def update_email(email, newEmail):
    conn = sql.connect('proje.db')
    cursor = conn.cursor()

    upd_command = """UPDATE USERS SET email = '{}' WHERE email = '{}' """
    cursor.execute(upd_command.format(newEmail, email))

    conn.commit()
    conn.close()

def delete_account(email):
    conn = sql.connect('proje.db')
    cursor = conn.cursor()

    dlt_command = """DELETE from USERS WHERE email = '{}' """
    cursor.execute(dlt_command.format(email))

    conn.commit()
    conn.close()


def rezervasyonlar(email, newRezervasyon):
    conn = sql.connect('proje.db')
    cursor = conn.cursor()

    upd_command = """UPDATE USERS SET rezervasyonlar = '{}' WHERE email = '{}' """
    cursor.execute(upd_command.format(newRezervasyon, email))

    conn.commit()
    conn.close()

