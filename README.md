## BELAJAR FLASK MAHIR

```cmd
git init
git add .
git commit -m "first commit"
git branch -M 01_python
git remote add origin https://github.com/edycoleee/flask2.git
git push -u origin 01_python

git branch 02_gethalo
git checkout 02_gethalo
```

MATERI

| Branch            | Keterangan                            |
| ----------------- | ------------------------------------- |
| `01_python`       | Belajar Python dasar (`coba.py`)      |
| `02_gethalo`      | API sederhana `GET /halo`             |
| `03_cleanhalo`    | Clean code untuk `GET /halo`          |
| `04_nama`         | API dengan path `GET /nama/silmi`     |
| `05_posthalo`     | API dengan request body `POST /halo`  |
| `06_readall`      | Endpoint `GET /siswa`                 |
| `07_readallclean` | Clean code untuk `GET /siswa`         |
| `08_create`       | Endpoint `POST /siswa`                |
| `09_readone`      | Endpoint `GET /siswa/<id>`            |
| `10_delete`       | Endpoint `DELETE /siswa/<id>`         |
| `11_update`       | Endpoint `PUT /siswa/<id>`            |
| `12_register`     | Endpoint `POST /register`             |
| `13_login`        | Endpoint `POST /login`                |
| `14_logout`       | Endpoint `POST /logout`               |
| `15_crudauth`     | CRUD siswa dengan autentikasi         |
| `16_testcrud`     | Testing CRUD siswa dengan autentikasi |
| `17_docker`       | Deploy Docker                         |
| `18_postgre`      | Database Postgree > Docker            |

### 1. BELAJAR PYTHON

#### branch 01_python

- DECORATOR
  Decorator adalah fungsi yang menerima fungsi lain sebagai argumen, dan mengembalikannya (atau versi modifikasinya).

```py
#Bentuk dasar:
def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dijalankan")
        func()
        print("Setelah fungsi dijalankan")
    return wrapper

#Lalu dipakai seperti ini:
@my_decorator
def say_hello():
    print("Halo dunia")

say_hello()
#Output:
Sebelum fungsi dijalankan
Halo dunia
Setelah fungsi dijalankan
# @my_decorator adalah cara singkat untuk menulis:
say_hello = my_decorator(say_hello)

# Decorator dengan Parameter
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def halo():
    print("Halo!")

halo()

# Output:
Halo!
Halo!
Halo!
```

```js
// Jika menggunakan js seperti ini
function myDecorator(func) {
    return function () {
        console.log("Sebelum fungsi dijalankan");
        func();
        console.log("Setelah fungsi dijalankan");
    };
}

function sayHello() {
    console.log("Halo dunia");
}

// Bungkus fungsi menggunakan decorator
const decoratedSayHello = myDecorator(sayHello);

// Panggil fungsi yang sudah didekorasi
decoratedSayHello();

function repeat(n) {
    return function (func) {
        return function (...args) {
            for (let i = 0; i < n; i++) {
                func(...args);
            }
        };
    };
}

function halo() {
    console.log("Halo!");
}

// Bungkus fungsi halo dengan decorator repeat(3)
const decoratedHalo = repeat(3)(halo);

decoratedHalo();

```
- ARGS, KWARGS

Python biarkan kamu pakai \_ untuk "placeholder", mirip i pada js for (let i = 0; i < 3; i++) {console.log("Halo")}

```py
#  Contoh Python:
for _ in range(3):
    print("Halo")
# Output:
Halo
Halo
Halo
```

```py
#Contoh penggunaan kwargs
def halo(**kwargs):
    print(kwargs)

halo(nama="andi", usia=25)
```

```js
// kalau di JS seperti ini
function halo({ nama, usia }) {
  console.log({ nama, usia });
}

halo({ nama: "andi", usia: 25 });
```

```py
#Contoh args
def info(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

info(1, 2, nama="Eka", aktif=True)
#Output:
Args: (1, 2) # seperti array (list)
Kwargs: {'nama': 'Eka', 'aktif': True} # object (dict)

```

| Python     | Artinya                                 | Mirip di JavaScript  |
| ---------- | --------------------------------------- | -------------------- |
| `_`        | Placeholder variabel (tidak digunakan)  | `for (let _ of arr)` |
| `**kwargs` | Kumpulan keyword arguments → `dict`     | `function({ ... })`  |
| `*args`    | Kumpulan positional arguments → `tuple` | `function(...args)`  |

- DICT, LIST, TUPLE

```py
#dict di Python = object di JavaScript
user = {
    "nama": "Andi",
    "usia": 25
}
print(user["nama"])  # Output: Andi

#tuple di Python ≈ array dengan const di JavaScript
#array (tidak diubah)
lokasi = ("Jakarta", -6.2)
print(lokasi[0])  # Output: Jakarta

#Contoh list (mutable)
#array (bisa diubah)
buah = ["apel", "jeruk", "pisang"]
buah[0] = "mangga"           # Bisa diubah
buah.append("anggur")        # Bisa ditambah
print(buah)

```

| Konsep Python | Bentuk             | Mirip JavaScript           |
| ------------- | ------------------ | -------------------------- |
| `dict`        | `{ "key": value }` | object literal             |
| `tuple`       | `("val1", "val2")` | const array (tidak diubah) |
| `list`        | `[ "a", "b" ]`     | array                      |

- FUNCTION, IF ELSE

```py
def proses_data(data):
    if isinstance(data, list): #mengecek apakah data adalah list.
        print("Tipe: list")
        print("Isi:", data)
        print("Operasi: Menambah item 'baru'")
        data.append("baru")
        print("Hasil setelah append:", data)
    elif isinstance(data, tuple): #mengecek apakah data adalah tuple.
        print("Tipe: tuple")
        print("Isi:", data)
        print("Operasi: Tidak bisa diubah (immutable)")
        print("Coba ubah indeks 0 akan error jika dilakukan")
    else:
        print("Tipe data tidak dikenali")

# Contoh pemakaian:
data1 = ["apel", "jeruk"]
data2 = ("merah", "biru")

proses_data(data1)
print()  # Pemisah
proses_data(data2)

#Output:
Tipe: list
Isi: ['apel', 'jeruk']
Operasi: Menambah item 'baru'
Hasil setelah append: ['apel', 'jeruk', 'baru']

Tipe: tuple
Isi: ('merah', 'biru')
Operasi: Tidak bisa diubah (immutable)
Coba ubah indeks 0 akan error jika dilakukan

```

### 1. API SEDERHANA

#### branch 02_gethalo

| No  | Method | Endpoint       | Request Body (JSON)                         | Response (JSON)                             |
| --- | ------ | -------------- | ------------------------------------------- | ------------------------------------------- |
| 1   | GET    | `/halo`        | (tidak ada)                                 | `{ "message": "Belajar Flask" }`            |
| 2   | GET    | `/nama/<nama>` | (tidak ada)                                 | `{ "message": "Halo silmi" }`               |
| 3   | POST   | `/halo`        | `{ "nama": "Silmi", "alamat": "Semarang" }` | `{ "nama": "Silmi", "alamat": "Semarang" }` |

LANGKAH : ENVIRONTMENT >> app.py >> test_app.py >> TEST

app.py : import >> create object >> route(url,method) >> funtion return response >> run(python app.py)

test_app.py : import >> client >> function test >> assert response >> pytest

| No  | Method | Endpoint | Request Body (JSON) | Response (JSON)                  |
| --- | ------ | -------- | ------------------- | -------------------------------- |
| 1   | GET    | `/halo`  | (tidak ada)         | `{ "message": "Belajar Flask" }` |

```py
#project-folder/
#│
#├── app.py
#└── test_app.py

# 1. Membuat Virtual Environtment
python -m venv venv
source venv/bin/activate  #Linux / Macbook
venv\Scripts\activate # Windows

#2. Install Flask
pip install flask pytest flask_cors

#3. app.py
# import >> create object >> route >> funtion return response >> run
#a. import Flask
from flask import Flask, jsonify
#b. create object app
app = Flask(__name__)
#c. create route, method
@app.route('/halo', methods=['GET'])
#d. create fungction with return as response
def halo():
    return jsonify({"message": "Belajar Flask"})
#e. runc object default/host,port
if __name__ == '__main__':
    app.run(debug=True)
#Jika dengan docker : app.run(host='0.0.0.0', port=5000, debug=True)

#4. Jalankan
python app.py

#5. Coba Di browser / Postman
http://127.0.0.1:5000/halo

{
    "message": "Belajar Flask"
}


#6. test_app.py
# import >> client >> function test >> assert response
import pytest
from app import app  # Import aplikasi Flask dari file app.py

@pytest.fixture
def client():
    # Setup Flask test client
    with app.test_client() as client:
        yield client

def test_hallo_endpoint(client):
    # Kirim request GET ke endpoint /hallo
    response = client.get('/halo')
    # Pastikan status kode adalah 200
    assert response.status_code == 200
    # Pastikan respon JSON sesuai
    assert response.get_json() == {"message": "Belajar Flask"}

#7. Jalankan Test
pytest
```

### 2. CLEAN CODE API SEDERHANA

#### branch 03_cleanhalo

LANGKAH : app.py >> routes >> docs >> test_app.py >> TEST

```
project-folder/
│
├── app.py
├── routes/
│   └── belajar.py
├── docs/
│   └── halo.yml
└── test/
    ├──__init__.py
    └── test_belajar.py

```

```py
# import >> create object >> cors,swagger >> route register >> run
# # # app.py >> ketiga dg cleancode
from flask import Flask
from flasgger import Swagger
from routes.belajar import belajar_bp  # perbaikan import
from flask_cors import CORS

app = Flask(__name__) #	asal root project-Flask dimulai pada file ini (app.py)
CORS(app)  # Aktifkan CORS untuk semua route
app.config['SWAGGER'] = {
    'title': 'COBA API',
    'uiversion': 3
}
swagger = Swagger(app)

# Register blueprint >> Seperti Router() di Express
app.register_blueprint(belajar_bp)

if __name__ == '__main__':
    app.run(debug=True)

#/routes/belajar.py
from flask import Blueprint, jsonify
from flasgger import swag_from
import os

#'belajar_bp' (param 1)	Nama unik blueprint
# __name__ (param 2)	Nama modul Python → bantu Flask resolve file
belajar_bp = Blueprint('belajar_bp', __name__)

# route, method >> swagger doc >> function return response
@belajar_bp.route('/halo', methods=['GET'])
@swag_from('../docs/halo.yml')
def get_halo():
    return jsonify({"message": "Belajar Flask"})

#/test/test_belajar.py
# import >> client >> function test >> assert response
import pytest
from app import app  # Import aplikasi Flask dari file app.py

@pytest.fixture
def client():
    # Setup Flask test client
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hallo_endpoint(client):
    # Kirim request GET ke endpoint /hallo
    response = client.get('/halo')
    # Pastikan status kode adalah 200
    assert response.status_code == 200
    # Pastikan respon JSON sesuai
    assert response.get_json() == {"message": "Belajar Flask"}
```

```yml
# Dokumentasi >> tag >> response >> schema >> properties >> {}
# halo.yml
---
tags: #Judul
  - Halo
responses:
  200: #Respon status
    description: Respon sukses #Deskripsi status
    schema:
      type: object #Tipe data response body
      properties:
        message: #key object
          type: string #tipe value object
          example: Halo Flask #contoh value object
```

### 3. API SEDERHANA LANJUTAN

#### branch 04_nama

LANGKAH : app.py >> test_app.py >> TEST

| No  | Method | Endpoint       | Request Body (JSON) | Response (JSON)               |
| --- | ------ | -------------- | ------------------- | ----------------------------- |
| 2   | GET    | `/nama/<nama>` | (tidak ada)         | `{ "message": "Halo silmi" }` |

```py
# tambahkan #/routes/belajar.py
# route, method >> swagger doc >> function return response
@belajar_bp.route('/nama/<nama>', methods=['GET'])
@swag_from('../docs/nama.yml')
def halo_nama(nama):
    return jsonify({"message": f"Halo {nama}"})

# function test >> assert response
#/test/test_belajar.py
def test_halo_nama(client):
    response = client.get('/nama/silmi')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Halo silmi"}
```

```yml
tags:
  - Belajar API GET POST #Judul
parameters:
  - in: path #params pada header
    name: nama #nama variabel
    type: string #tipe
    required: true
    description: Nama pengguna yang ingin disapa
responses:
  200:
    description: Respons sukses
    schema:
      type: object
      properties:
        message:
          type: string
          example: Halo silmi
```

#### branch 05_posthalo

LANGKAH : app.py >> test_app.py >> TEST

| No  | Method | Endpoint | Request Body (JSON)                         | Response (JSON)                             |
| --- | ------ | -------- | ------------------------------------------- | ------------------------------------------- |
| 3   | POST   | `/halo`  | `{ "nama": "Silmi", "alamat": "Semarang" }` | `{ "nama": "Silmi", "alamat": "Semarang" }` |

```py
# tambahkan #/routes/belajar.py
# route, method >> swagger doc >> function >> get request data >> return response
@belajar_bp.route('/halo', methods=['POST'])
@swag_from('../docs/halo_post.yml')
def halo_post():
    from flask import request
    data = request.get_json()
    return jsonify({
        "nama": data.get("nama"),
        "alamat": data.get("alamat")
    })

#tambahkan #/test/test_belajar.py
# function test >> payload ke body >> assert response
def test_post_halo(client):
    payload = {"nama": "Silmi", "alamat": "Semarang"}
    response = client.post('/halo', json=payload)
    assert response.status_code == 200
    assert response.get_json() == payload
```

```yml
---
# Dokumentasi >> tag >> response >> schema >> properties >> {}
tags:
  - Belajar API GET POST
parameters:
  - in: body # request body
    name: body
    required: true
    schema:
      type: object
      required: # semua key
        - nama
        - alamat
      properties: # semua value >> tipe >> example
        nama:
          type: string
          example: Silmi
        alamat:
          type: string
          example: Semarang
responses:
  200:
    description: Data berhasil diterima
    schema: # reresponse body
      type: object
      properties:
        nama:
          type: string
        alamat:
          type: string
```

### 3. CRUD API

#### branch 06_readall

| No  | Method | Endpoint      | Request Body (JSON)                                | Response (JSON)                                               |
| --- | ------ | ------------- | -------------------------------------------------- | ------------------------------------------------------------- |
| 1   | POST   | `/siswa`      | `{ "nama": "Silmi", "alamat": "Semarang" }`        | `{ "message": "Siswa berhasil ditambahkan" }`                 |
| 2   | GET    | `/siswa`      | (tidak ada)                                        | `[ { "id": 1, "nama": "Silmi", "alamat": "Semarang" }, ... ]` |
| 3   | GET    | `/siswa/<id>` | (tidak ada)                                        | `{ "id": 1, "nama": "Silmi", "alamat": "Semarang" }`          |
| 4   | PUT    | `/siswa/<id>` | `{ "nama": "Silmi Updated", "alamat": "Jakarta" }` | `{ "message": "Siswa berhasil diperbarui" }`                  |
| 5   | DELETE | `/siswa/<id>` | (tidak ada)                                        | `{ "message": "Siswa berhasil dihapus" }`                     |

LANGKAH : app.py >> routes >> services >> docs >> test_siswa.py >> TEST

project-folder/
├── app.py
├── routes/
│ ├── siswa.py ← Semua endpoint siswa
│ └── belajar.py ← Endpoint halo dan nama
├── docs/ ← Swagger YAML
│ ├── siswa_create.yml
│ ├── siswa_delete.yml
│ ├── siswa_update.yml
│ ├── siswa_read_all.yml
│ ├── siswa_read_id.yml
│ ├── nama.yml
│ ├── halo_post.yml
│ └── halo.yml
├── test/
│ ├── **init**.py
│ ├── test_siswa.py
│ └── test_belajar.py
└── siswa.db ← File SQLite (otomatis dibuat)

```py
# # # app.py
#.....
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

init_db()

# Register Blueprint >> siswa
from routes.siswa import siswa_bp

app.register_blueprint(siswa_bp)
```

PELAJARAN SQL

| METHOD   | PATH/ID | REQ BODY | QUERY SQL                                                                              | CURSOR SQL          |
| -------- | ------- | -------- | -------------------------------------------------------------------------------------- | ------------------- |
| READ ALL | -       | -        | `SELECT * FROM tb_siswa`                                                               | `cursor.fetchall()` |
| CREATE   | -       | body     | `INSERT INTO tb_siswa (nama, alamat) VALUES (?, ?)` `(data['nama'], data['alamat'])`   | -                   |
| READ ONE | id      | -        | `SELECT * FROM tb_siswa WHERE id=?` `(id,)`                                            | `cursor.fetchone()` |
| DELETE   | id      | -        | `DELETE FROM tb_siswa WHERE id=?` `(id,)`                                              | -                   |
| UPDATE   | id      | body     | `UPDATE tb_siswa SET nama=?, alamat=? WHERE id=?` `(data['nama'], data['alamat'], id)` | -                   |

FUNGSI CURSOR SQL LAINNYA

| Fungsi         | Deskripsi Singkat                    | Return Tipe        | Kapan Digunakan                                  |
| -------------- | ------------------------------------ | ------------------ | ------------------------------------------------ |
| `fetchall()`   | Mengambil semua baris                | List of tuple/dict | Jika datanya kecil/sedang                        |
| `fetchone()`   | Mengambil satu baris (per panggilan) | Tuple/dict         | Jika hanya butuh 1 baris atau mau looping manual |
| `fetchmany(n)` | Mengambil `n` baris                  | List of tuple/dict | Jika ingin baca bertahap (misal data besar)      |

PERINTAH SQL PADA PYTHON - SQLITE

```py
with sqlite3.connect('siswa.db') as conn:   # 1 membuat koneksi sql
  cursor = conn.cursor()                    # 2 membuat object cursor
  cursor.execute("SELECT * FROM tb_siswa")  # 3 eksekusi perintah sql
  rows = cursor.fetchall()                  # 4 jika operasi sql dg variabel kembali (rows)
  #conn.commit()                            # 4 jika operasi sql tanpa variabel kembali
```

- READ ALL

```py
#routes/siswa.py
#route, method >> swagger doc >> function (SQL return response)
from flask import Blueprint, request, jsonify
from flasgger.utils import swag_from
import sqlite3

siswa_bp = Blueprint('siswa', __name__)

@siswa_bp.route('/siswa', methods=['GET'])
@swag_from('../docs/siswa_read_all.yml')
def get_all_siswa():
    with sqlite3.connect('siswa.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tb_siswa")
        rows = cursor.fetchall()
    result = [{"id": row[0], "nama": row[1], "alamat": row[2]} for row in rows]
    return jsonify(result)

#/test/test_siswa.py
# client >> function test >> get(url) >> assert response
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_all_siswa(client):
    response = client.get('/siswa')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
```

```yml
#/docs/siswa_read_all >> response array object >> [{}]
---
tags:
  - Siswa
responses:
  200:
    description: Daftar semua siswa
    schema:
      type: array
      items:
        type: object
        properties:
          id:
            type: integer
          nama:
            type: string
          alamat:
            type: string
```

- READ ALL WITH SERVICES

#### branch 07_readallclean

```py
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

#routes/siswa.py
#route, method >> swagger doc >> function (try >> service.readall return response >> except error)
from flask import Blueprint, request, jsonify
from flasgger import swag_from
from services import siswa_service

siswa_bp = Blueprint('siswa', __name__)

@siswa_bp.route('/siswa', methods=['GET'])
@swag_from('docs/siswa_read_all.yml')
def read_all_siswa():
    try:
        data = siswa_service.read_all_siswa()
        return jsonify(data), 200
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Gagal mengambil data"}), 500

```

- CREATE

#### branch 08_create

```py
#services/siswa_service.py
#...
def create_siswa(nama, alamat):
    conn = get_db_connection()
    conn.execute("INSERT INTO tb_siswa (nama, alamat) VALUES (?, ?)", (nama, alamat))
    conn.commit()
    conn.close()

#routes/siswa.py
#...
@siswa_bp.route('/siswa', methods=['POST'])
@swag_from('docs/siswa_create.yml')
def create_siswa():
    try:
        data = request.get_json()
        siswa_service.create_siswa(data['nama'], data['alamat'])
        return jsonify({"message": "Siswa berhasil ditambahkan"}), 201
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Gagal menambahkan siswa"}), 500

#test/test_siswa.py
#...
def test_create_siswa(client):
    response = client.post('/siswa', json={"nama": "Budi", "alamat": "Jogja"})
    assert response.status_code == 201
    assert response.json['message'] == "Siswa berhasil ditambahkan"
```

```yml
#request body >> object >> detail object >> response code >> response
#docs/siswa_create.yml
---
tags:
  - Siswa
parameters:
  - in: body
    name: body
    required: true
    schema:
      type: object
      required:
        - nama
        - alamat
      properties:
        nama:
          type: string
          example: Budi
        alamat:
          type: string
          example: Jakarta
responses:
  201:
    description: Siswa berhasil ditambahkan
    content:
      application/json:
        example:
          message: Siswa berhasil ditambahkan
  500:
    description: Gagal menambahkan siswa
```

- READ ONE

#### branch 09_readone

```py
#services/siswa_service.py
#...
def read_siswa_by_id(id):
    conn = get_db_connection()
    row = conn.execute("SELECT id, nama, alamat FROM tb_siswa WHERE id = ?", (id,)).fetchone()
    conn.close()
    return dict(row) if row else None

#routes/siswa.py
#...
@siswa_bp.route('/siswa/<int:id>', methods=['GET'])
@swag_from('docs/siswa_read_id.yml')
def read_siswa_by_id(id):
    try:
        data = siswa_service.read_siswa_by_id(id)
        if data:
            return jsonify(data), 200
        return jsonify({"error": "Siswa tidak ditemukan"}), 404
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Gagal mengambil data"}), 500

#test/test_siswa.py
#...
def test_read_siswa_by_id(client):
    response = client.get('/siswa/1')
    assert response.status_code in [200, 404]
```

```yml
#siswa_read_id.yml
---
tags:
  - Siswa
parameters:
  - name: id
    in: path
    type: integer
    required: true
    description: ID siswa
responses:
  200:
    description: Detail siswa berdasarkan ID
    schema:
      type: object
      properties:
        id:
          type: integer
        nama:
          type: string
        alamat:
          type: string
  404:
    description: Siswa tidak ditemukan
```

- DELETE

#### branch 10_delete

```py
#services/siswa_service.py
#...
def delete_siswa(id):
    conn = get_db_connection()
    cur = conn.execute("DELETE FROM tb_siswa WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return cur.rowcount

#routes/siswa.py
#...
@siswa_bp.route('/siswa/<int:id>', methods=['DELETE'])
@swag_from('docs/siswa_delete.yml')
def delete_siswa(id):
    try:
        deleted = siswa_service.delete_siswa(id)
        if deleted:
            return jsonify({"message": "Siswa berhasil dihapus"}), 200
        return jsonify({"error": "Siswa tidak ditemukan"}), 404
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Gagal menghapus siswa"}), 500

#test/test_siswa.py
#...
def test_delete_siswa(client):
    response = client.delete('/siswa/1')
    assert response.status_code in [200, 404]
```

```yml
#docs/siswa_delete.yml
---
tags:
  - Siswa
parameters:
  - name: id
    in: path
    type: integer
    required: true
    description: ID siswa yang akan dihapus
responses:
  200:
    description: Siswa berhasil dihapus
  404:
    description: Siswa tidak ditemukan
```

- UPDATE

#### branch 11_update

```py
#services/siswa_service.py
#...
def update_siswa(id, nama, alamat):
    conn = get_db_connection()
    cur = conn.execute("UPDATE tb_siswa SET nama = ?, alamat = ? WHERE id = ?", (nama, alamat, id))
    conn.commit()
    conn.close()
    return cur.rowcount

#routes/siswa.py
#...
@siswa_bp.route('/siswa/<int:id>', methods=['PUT'])
@swag_from('docs/siswa_update.yml')
def update_siswa(id):
    try:
        data = request.get_json()
        updated = siswa_service.update_siswa(id, data['nama'], data['alamat'])
        if updated:
            return jsonify({"message": "Siswa berhasil diperbarui"}), 200
        return jsonify({"error": "Siswa tidak ditemukan"}), 404
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Gagal memperbarui siswa"}), 500

#test/test_siswa.py
#...
def test_update_siswa(client):
    response = client.put('/siswa/1', json={"nama": "Silmi Update", "alamat": "Bandung"})
    assert response.status_code in [200, 404]

```

```yml
#siswa_update.yml
---
tags:
  - Siswa
parameters:
  - name: id
    in: path
    type: integer
    required: true
    description: ID siswa yang akan diupdate
  - in: body
    name: body
    required: true
    schema:
      type: object
      required:
        - nama
        - alamat
      properties:
        nama:
          type: string
          example: Update Nama
        alamat:
          type: string
          example: Update Alamat
responses:
  200:
    description: Siswa berhasil diperbarui
  404:
    description: Siswa tidak ditemukan
```

### 5. AUTH API

| No  | Method | URL       | Request JSON                                     | Response JSON (Berhasil)                          | Response JSON (Gagal)                                             |
| --- | ------ | --------- | ------------------------------------------------ | ------------------------------------------------- | ----------------------------------------------------------------- |
| 1   | POST   | /register | `{ "username": "user1", "password": "pass123" }` | `{ "message": "Registrasi berhasil" }`            | `409 Conflict`: `{ "error": "Username sudah digunakan" }`         |
| 2   | POST   | /login    | `{ "username": "user1", "password": "pass123" }` | `{ "message": "Login berhasil", "token": "..." }` | `401 Unauthorized`: `{ "error": "Username atau password salah" }` |
| 3   | POST   | /logout   | (Header: `Authorization: Bearer <token>`)        | `{ "message": "Logout berhasil" }`                | `401 Unauthorized`: `{ "error": "Token tidak valid" }`            |

```cmd

project-folder/
│
├── app.py
├── middleware/
│ └── auth_middleware.py ← 🆕 Di sini tempatnya token_required
├── routes/
│ ├── siswa.py
│ └── auth.py
├── services/
│ └── siswa_service.py
...
```

```py
#1. Tabel tb_user
#Tambahkan ini di init_db() di app.py:

conn.execute('''
    CREATE TABLE IF NOT EXISTS tb_user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        token TEXT
    )
''')
```

- REGISTER

#### branch 12_register

```py
#/routes/auth.py
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
    username = data.get('username')
    password = hash_password(data.get('password'))

    try:
        with sqlite3.connect(DB) as conn:
            conn.execute("INSERT INTO tb_user (username, password) VALUES (?, ?)", (username, password))
        return jsonify({"message": "Registrasi berhasil"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username sudah digunakan"}), 409
#2. Register Blueprint di app.py
from routes.auth import auth_bp
app.register_blueprint(auth_bp)

#3. Tambahkan Middleware Auth (Opsional) middleware/auth_middleware.py
#Untuk mengamankan endpoint siswa, bisa buat decorator @token_required:
from functools import wraps
from flask import request, jsonify
import sqlite3

DB = 'siswa.db'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token diperlukan'}), 401
        with sqlite3.connect(DB) as conn:
            user = conn.execute("SELECT * FROM tb_user WHERE token = ?", (token,)).fetchone()
            if not user:
                return jsonify({'error': 'Token tidak valid'}), 401
        return f(*args, **kwargs)
    return decorated

#4. File: test/test_auth.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

username = "testuser"
password = "testpass"

def test_register(client):
    response = client.post('/register', json={
        "username": username,
        "password": password
    })
    assert response.status_code in [201, 409]  # 201 (baru), 409 (sudah ada)

#pytest test/test_auth.py
```

```yml
#auth/register.yml
tags:
  - Auth
parameters:
  - in: body
    name: body
    required: true
    schema:
      type: object
      required:
        - username
        - password
      properties:
        username:
          type: string
          example: silmi
        password:
          type: string
          example: silmi123
responses:
  201:
    description: Registrasi berhasil
  409:
    description: Username sudah digunakan
```

- LOGIN

#### branch 13_login

```py
#1. Folder routes/auth.py
#..................
@auth_bp.route('/login', methods=['POST'])
@swag_from('../docs/auth/login.yml')
def login():
    data = request.get_json()
    username = data.get('username')
    password = hash_password(data.get('password'))

    with sqlite3.connect(DB) as conn:
        user = conn.execute("SELECT * FROM tb_user WHERE username = ? AND password = ?", (username, password)).fetchone()
        if user:
            token = str(uuid.uuid4())
            conn.execute("UPDATE tb_user SET token = ? WHERE username = ?", (token, username))
            return jsonify({"message": "Login berhasil", "token": token}), 200
        return jsonify({"error": "Username atau password salah"}), 401

#2. File: test/test_auth.py
#...............
def test_login(client):
    response = client.post('/login', json={
        "username": username,
        "password": password
    })
    assert response.status_code == 200
    json_data = response.get_json()
    assert "token" in json_data
    # Simpan token untuk test berikutnya
    global TOKEN
    TOKEN = json_data["token"]
```

```yml
#auth/login.yml
tags:
  - Auth
parameters:
  - in: body
    name: body
    required: true
    schema:
      type: object
      required:
        - username
        - password
      properties:
        username:
          type: string
          example: silmi
        password:
          type: string
          example: silmi123
responses:
  200:
    description: Login berhasil, token dikembalikan
    schema:
      type: object
      properties:
        message:
          type: string
        token:
          type: string
  401:
    description: Username atau password salah
```

- LOGOUT

#### branch 14_logout

```py
#1. Folder routes/auth.py
#..................
@auth_bp.route('/logout', methods=['POST'])
@swag_from('../docs/auth/logout.yml')
def logout():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"error": "Token tidak ditemukan"}), 401

    with sqlite3.connect(DB) as conn:
        cur = conn.execute("UPDATE tb_user SET token = NULL WHERE token = ?", (token,))
        if cur.rowcount:
            return jsonify({"message": "Logout berhasil"}), 200
        return jsonify({"error": "Token tidak valid"}), 401

#2. File: test/test_auth.py
#............
def test_logout(client):
    headers = {"Authorization": TOKEN}
    response = client.post('/logout', headers=headers)
    assert response.status_code == 200
    assert response.get_json().get("message") == "Logout berhasil"
```

```yml
#auth/logout.yml
tags:
  - Auth
summary: Logout user berdasarkan token
produces:
  - application/json
parameters:
  - name: Authorization
    in: header
    required: true
    type: string
    description: Token user
responses:
  200:
    description: Logout berhasil
  401:
    description: Token tidak valid atau tidak ditemukan
```

### 5. AUTH API CRUD SISWA

- CRUD

#### branch 15_crudauth

```py
#routes/siswa.py
from flask import Blueprint, request, jsonify
from flasgger import swag_from
from middleware.auth_middleware import token_required
from services import siswa_service

siswa_bp = Blueprint('siswa', __name__)

@siswa_bp.route('/siswa', methods=['POST'])
@token_required
@swag_from('../docs/siswa/create.yml')
def create_siswa():
    try:
        data = request.get_json()
        siswa_service.create_siswa(data['nama'], data['alamat'])
        return jsonify({"message": "Siswa berhasil ditambahkan"}), 201
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Gagal menambahkan siswa"}), 500

@siswa_bp.route('/siswa', methods=['GET'])
@token_required
@swag_from('../docs/siswa/read_all.yml')
def read_all_siswa():
    try:
        data = siswa_service.read_all_siswa()
        return jsonify(data), 200
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Gagal mengambil data"}), 500

@siswa_bp.route('/siswa/<int:id>', methods=['GET'])
@token_required
@swag_from('../docs/siswa/read_id.yml')
def read_siswa_by_id(id):
    try:
        data = siswa_service.read_siswa_by_id(id)
        if data:
            return jsonify(data), 200
        return jsonify({"error": "Siswa tidak ditemukan"}), 404
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Gagal mengambil data"}), 500

@siswa_bp.route('/siswa/<int:id>', methods=['PUT'])
@token_required
@swag_from('../docs/siswa/update.yml')
def update_siswa(id):
    try:
        data = request.get_json()
        updated = siswa_service.update_siswa(id, data['nama'], data['alamat'])
        if updated:
            return jsonify({"message": "Siswa berhasil diperbarui"}), 200
        return jsonify({"error": "Siswa tidak ditemukan"}), 404
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Gagal memperbarui siswa"}), 500

@siswa_bp.route('/siswa/<int:id>', methods=['DELETE'])
@token_required
@swag_from('../docs/siswa/delete.yml')
def delete_siswa(id):
    try:
        deleted = siswa_service.delete_siswa(id)
        if deleted:
            return jsonify({"message": "Siswa berhasil dihapus"}), 200
        return jsonify({"error": "Siswa tidak ditemukan"}), 404
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Gagal menghapus siswa"}), 500
```

```yml
#docs/siswa/delete.yml
---
tags:
  - Siswa
summary: Hapus siswa berdasarkan ID
security:
  - ApiKeyAuth: []
parameters:
  - name: Authorization
    in: header
    required: true
    type: string
    description: Token autentikasi
  - name: id
    in: path
    required: true
    type: integer
    description: ID siswa
responses:
  200:
    description: Siswa berhasil dihapus
    schema:
      type: object
      properties:
        message:
          type: string
  404:
    description: Siswa tidak ditemukan
  500:
    description: Gagal menghapus siswa

#docs/siswa/update.yml
---
tags:
  - Siswa
summary: Perbarui data siswa berdasarkan ID
security:
  - ApiKeyAuth: []
parameters:
  - name: Authorization
    in: header
    required: true
    type: string
    description: Token autentikasi
  - name: id
    in: path
    required: true
    type: integer
    description: ID siswa
  - in: body
    name: body
    required: true
    schema:
      type: object
      required:
        - nama
        - alamat
      properties:
        nama:
          type: string
        alamat:
          type: string
responses:
  200:
    description: Siswa berhasil diperbarui
    schema:
      type: object
      properties:
        message:
          type: string
  404:
    description: Siswa tidak ditemukan
  500:
    description: Gagal memperbarui siswa

#docs/siswa/read_id.yml
---
tags:
  - Siswa
summary: Ambil data siswa berdasarkan ID
security:
  - ApiKeyAuth: []
parameters:
  - name: Authorization
    in: header
    required: true
    type: string
    description: Token autentikasi
  - name: id
    in: path
    required: true
    type: integer
    description: ID siswa
responses:
  200:
    description: Data siswa ditemukan
    schema:
      type: object
      properties:
        id:
          type: integer
        nama:
          type: string
        alamat:
          type: string
  404:
    description: Siswa tidak ditemukan
  500:
    description: Gagal mengambil data

#docs/siswa/create.yml
---
tags:
  - Siswa
summary: Tambah siswa baru
security:
  - ApiKeyAuth: []
parameters:
  - name: Authorization
    in: header
    required: true
    type: string
    description: Token autentikasi
  - in: body
    name: body
    required: true
    schema:
      type: object
      required:
        - nama
        - alamat
      properties:
        nama:
          type: string
        alamat:
          type: string
responses:
  201:
    description: Siswa berhasil ditambahkan
    schema:
      type: object
      properties:
        message:
          type: string
  500:
    description: Gagal menambahkan siswa
    schema:
      type: object
      properties:
        error:
          type: string
```

- TEST

#### branch 16_testcrud

```py
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def auth_headers(client):
    # Register
    client.post('/register', json={"username": "testuser", "password": "testpass"})

    # Login
    response = client.post('/login', json={"username": "testuser", "password": "testpass"})
    token = response.get_json().get('token')

    return {
        "Authorization": token
    }

def test_create_siswa(client, auth_headers):
    response = client.post('/siswa', headers=auth_headers, json={
        "nama": "Test", "alamat": "Bandung"
    })
    assert response.status_code == 201
    assert b"Siswa berhasil ditambahkan" in response.data

def test_get_all_siswa(client, auth_headers):
    response = client.get('/siswa', headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_siswa_by_id(client, auth_headers):
    # Buat siswa
    create = client.post('/siswa', headers=auth_headers, json={"nama": "Andi", "alamat": "Jogja"})
    assert create.status_code == 201

    # Ambil siswa terakhir
    siswa = client.get('/siswa', headers=auth_headers).get_json()[-1]
    id_siswa = siswa['id']

    # Test ambil berdasarkan ID
    response = client.get(f'/siswa/{id_siswa}', headers=auth_headers)
    assert response.status_code == 200
    assert response.get_json()['nama'] == "Andi"

def test_update_siswa(client, auth_headers):
    # Buat siswa
    client.post('/siswa', headers=auth_headers, json={"nama": "Budi", "alamat": "Solo"})
    siswa = client.get('/siswa', headers=auth_headers).get_json()[-1]
    id_siswa = siswa['id']

    # Update
    response = client.put(f'/siswa/{id_siswa}', headers=auth_headers, json={
        "nama": "Budi Update", "alamat": "Solo Baru"
    })
    assert response.status_code == 200
    assert b"Siswa berhasil diperbarui" in response.data

def test_delete_siswa(client, auth_headers):
    # Buat siswa
    client.post('/siswa', headers=auth_headers, json={"nama": "Citra", "alamat": "Bogor"})
    siswa = client.get('/siswa', headers=auth_headers).get_json()[-1]
    id_siswa = siswa['id']

    # Hapus siswa
    response = client.delete(f'/siswa/{id_siswa}', headers=auth_headers)
    assert response.status_code == 200
    assert b"Siswa berhasil dihapus" in response.data

    # Pastikan sudah dihapus
    check = client.get(f'/siswa/{id_siswa}', headers=auth_headers)
    assert check.status_code == 404
```

### 6. DEPLOY KE DOCKER

#### branch 17_docker

### 7. GUNAKAN DATABASE POSTGREE > DOCKER

#### branch 18_postgre
