from flask import Blueprint, request, jsonify
import sqlite3, uuid, hashlib
from flasgger.utils import swag_from

auth_bp = Blueprint('auth', __name__)
DB = 'siswa.db'

#password di hash supaya tdk bisa di baca langsung
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#register : url,method >> req body {username, password} >> insert tb_user
@auth_bp.route('/register', methods=['POST'])
@swag_from('../docs/auth/register.yml')
def register():
    data = request.get_json()

    # Validasi input
    if not data or 'username' not in data or 'password' not in data:
      return jsonify({"error": "Field 'username' dan 'password' wajib diisi"}), 400

    username = data.get('username')
    password = hash_password(data.get('password'))

    try:
        with sqlite3.connect(DB) as conn:
            conn.execute("INSERT INTO tb_user (username, password) VALUES (?, ?)", (username, password))
        return jsonify({"message": "Registrasi berhasil"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username sudah digunakan"}), 409