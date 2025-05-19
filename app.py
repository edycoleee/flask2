#a. import Flask
import sqlite3
from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger

#b. create object app
app = Flask(__name__)

CORS(app)  # Aktifkan CORS untuk semua route
app.config['SWAGGER'] = {
    'title': 'COBA API',
    'uiversion': 3
}
swagger = Swagger(app)

# Inisialisasi DB >> membuat db dan create table
def init_db():
    with sqlite3.connect('siswa.db') as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS tb_siswa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama TEXT NOT NULL,
                alamat TEXT NOT NULL
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS tb_user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                token TEXT
            )
        ''')

init_db()

#c. create route, method
# Register blueprint >> Seperti Router() di Express
from routes.belajar import belajar_bp  # perbaikan import
# Register Blueprint >> siswa
from routes.siswa import siswa_bp
from routes.auth import auth_bp

app.register_blueprint(auth_bp)
app.register_blueprint(siswa_bp)
app.register_blueprint(belajar_bp)

#e. runc object default/host,port
if __name__ == '__main__':
    app.run(debug=True)
#Jika dengan docker : app.run(host='0.0.0.0', port=5000, debug=True)