import sqlite3
from flask import request


class Admin:
    def __init__(self):
        self.email = request.form['username']
        self.password = request.form['password']

    def validasi_admin(self):
        conn = sqlite3.connect('users.db')
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        cursor.execute("SELECT password FROM admin WHERE email = ?", (self.email,))

        result = cursor.fetchone()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        if result is not None:
            if self.password == result[0]:
                return True
        else:
            return False


    def input_data_krs(self):
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

    def update_nilai(self):
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