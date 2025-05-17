#routes/siswa.py
#route, method >> swagger doc >> function (try >> service.readall return response >> except error)
from flask import Blueprint, request, jsonify
from flasgger import swag_from
from services import siswa_service

siswa_bp = Blueprint('siswa', __name__)

#- READ ALL
@siswa_bp.route('/siswa', methods=['GET'])
@swag_from('../docs/siswa_read_all.yml')
def read_all_siswa():
    try:
        data = siswa_service.read_all_siswa()
        return jsonify({
            "message": "Daftar siswa berhasil diambil",
            "data": data
        }), 200
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Gagal mengambil data siswa"}), 500

#- CREATE
