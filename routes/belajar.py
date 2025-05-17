#/routes/belajar.py
from flask import Blueprint, jsonify
from flasgger import swag_from
import os

#'belajar_bp' (param 1)	Nama unik blueprint
# __name__ (param 2)	Nama modul Python → bantu Flask resolve file
belajar_bp = Blueprint('belajar_bp', __name__)

# route, method >> swagger doc >> function return response
@belajar_bp.route('/halo', methods=['GET'])
@swag_from('../docs/gethalo.yml')
def get_halo():
    return jsonify({"message": "Belajar Flask"})

# tambahkan #/routes/belajar.py
# route, method >> swagger doc >> function return response
@belajar_bp.route('/nama/<nama>', methods=['GET'])
@swag_from('../docs/nama.yml')
def halo_nama(nama):
    return jsonify({"message": f"Halo {nama}"})

# tambahkan #/routes/belajar.py
# route, method >> swagger doc >> function >> get request data >> return response
@belajar_bp.route('/halo', methods=['POST'])
@swag_from('../docs/posthalo.yml')
def halo_post():
    from flask import request
    data = request.get_json()
    return jsonify({
        "nama": data.get("nama"),
        "alamat": data.get("alamat")
    })