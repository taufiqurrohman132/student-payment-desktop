import sqlite3
import os

class MahasiswaModel:
    def __init__(self):
        self.conn = sqlite3.connect("DBPembayaran.db")
        self.cursor = self.conn.cursor()
        print("Menggunakan database:", os.path.abspath("DBPembayaran.db"))

    def simpan(self, nama, nim, prodi, fakultas, tahun_masuk):
        self.conn.execute(
            """INSERT INTO tbmhs (nama, nim, prodi, fakultas, tahunmasuk)
             VALUES (?,?,?,?,?) """, (nama, nim, prodi, fakultas, tahun_masuk)
        )
        self.conn.commit()

    def ambil_data(self, kolom, arah, status=None):
        query = "SELECT nama, nim, prodi, fakultas, tahunmasuk, status FROM tbmhs"
        params = []

        if status:
            query += " WHERE status = ?"
            params.append(status)

        query += f" ORDER BY {kolom} {arah}"

        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def ambil_data_by_nim(self, nim):
        self.cursor.execute(
            f"SELECT * FROM tbmhs WHERE nim={nim}"            
        )
        return self.cursor.fetchall()


    
    def hapus_data(self, nim):
        query = "DELETE FROM tbmhs WHERE nim = ?"
        self.cursor.execute(query, (nim,))
        self.conn.commit()

        

