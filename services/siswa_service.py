#services/siswa_service.py
# funct connection >> return object connection
import sqlite3

DATABASE = 'siswa.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

#get connect >> execute >> close >> return data
def read_all_siswa():
    conn = get_db_connection()
    siswa = conn.execute("SELECT id, nama, alamat FROM tb_siswa").fetchall()
    conn.close()
    return [dict(row) for row in siswa]

def create_siswa(nama, alamat):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tb_siswa (nama, alamat) VALUES (?, ?)",
        (nama, alamat)
    )
    conn.commit()
    siswa_id = cursor.lastrowid
    conn.close()
    return siswa_id