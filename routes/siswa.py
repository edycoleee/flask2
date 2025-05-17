#routes/siswa.py
#route, method >> swagger doc >> function (SQL return response)
from flask import Blueprint, request, jsonify
from flasgger.utils import swag_from
import sqlite3

siswa_bp = Blueprint('siswa', __name__)

@siswa_bp.route('/siswa', methods=['GET'])
@swag_from('../docs/siswa_read_all.yml')
def get_all_siswa():
    #1. connection
    with sqlite3.connect('siswa.db') as conn:
        # 2. cursor >> seperti object koneksi
        cursor = conn.cursor()
        # 3. excecute SQL
        cursor.execute("SELECT * FROM tb_siswa")
        # 4. rows >> festchall >> array object [{}]
        rows = cursor.fetchall()
    # result di bentuk seperti json format
    result = [{"id": row[0], "nama": row[1], "alamat": row[2]} for row in rows]
    return jsonify({
            "message": "Daftar siswa berhasil diambil",
            "data": result
        }), 200