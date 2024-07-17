import sqlite3
from flask import request


def create_akun():
    conn = sqlite3.connect('users.db')
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Create a table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        password TEXT NOT NULL
                    )''')
    conn.commit()
    # username = request.form['nama']
    insert_query = "INSERT INTO users (name, email, password) VALUES (?, ?, ?)"
    data = (request.form['nama'], request.form['gmail'], request.form['pass'])

    cursor.execute(insert_query, data)
    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()


def validasi():
    conn = sqlite3.connect('users.db')
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    email = request.form['username']
    password = request.form['password']

    cursor.execute("SELECT password FROM users WHERE email = ?", (email,))

    result = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    if result is not None:
        if password == result[0]:
            return True
    else:
        return False


def validasi_admin():
    conn = sqlite3.connect('users.db')
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    email = request.form['username']
    password = request.form['password']

    cursor.execute("SELECT password FROM admin WHERE email = ?", (email,))

    result = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    if result is not None:
        if password == result[0]:
            return True
    else:
        return False


def input_data_krs():
    conn = sqlite3.connect('users.db')
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # username = request.form['nama']
    insert_query = "INSERT INTO KRS (dosen, kelas, Hari_Waktu, matkul) VALUES (?, ?, ?, ?)"
    data = (request.form["dosen"], request.form['kelas'], request.form['jadwal'], request.form["matkul"])

    cursor.execute(insert_query, data)
    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()


def data_krs():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Execute the SQL query to retrieve all values from the 'users' table
    cursor.execute('SELECT * FROM KRS')

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Close the cursor and the connection
    cursor.close()
    conn.close()

    hasil = []

    for row in rows:
        row = {"id": f"{row[0]}", "dosen": row[1], "kelas": row[2],
               "jadwal": row[3], "nilai": row[4], "matkul": row[5], "siswa": row[6]}
        hasil.append(row)

    return hasil


def isi_krs(username):
    conn = sqlite3.connect('users.db')
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    email = username
    pilihan = request.form['krs']

    cursor.execute("SELECT name FROM users WHERE email = ?", (email,))

    result = cursor.fetchone()

    cursor.execute('UPDATE KRS SET siswa = ? WHERE id_matkul = ?', (result[0], pilihan))
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()


def data_siswa(email):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM users WHERE email = ?", (email,))

    result = cursor.fetchone()
    # Execute the SQL query to retrieve all values from the 'users' table
    cursor.execute("SELECT * FROM KRS WHERE siswa = ?", (result[0],))

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Close the cursor and the connection
    cursor.close()
    conn.close()

    hasil = []

    for row in rows:
        row = {"id": f"{row[0]}", "dosen": row[1], "kelas": row[2],
               "jadwal": row[3], "nilai": row[4], "matkul": row[5], "siswa": row[6]}
        hasil.append(row)

    return hasil


def update_nilai():
    conn = sqlite3.connect('users.db')
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    nilai = request.form['nilai']
    pilihan = request.form['krs']

    cursor.execute('UPDATE KRS SET nilai = ? WHERE id_matkul = ?', (nilai, pilihan))
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()


if __name__ == '__main__':
    # Create a table
    '''CREATE TABLE IF NOT EXISTS admin (
            id_admin INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )'''

    # conn = sqlite3.connect('users.db')
    # # Create a cursor object to execute SQL queries
    # cursor = conn.cursor()
    #
    # # Create a table
    # cursor.execute('''ALTER TABLE KRS
    #             ADD COLUMN siswa TEXT;
    #         ''')
    #
    # conn.commit()
    # conn.close()
