## BELAJAR FLASK MAHIR

**Push ke Github Pertama Kali**

```cmd
git init
git add .
git commit -m "first commit"
git branch -M 01_python
git remote add origin https://github.com/edycoleee/flask2.git
git push -u origin 01_python
```

**_MATERI YANG DIPELAJARI_**

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

LATIHAN : buat 2 funct untuk decorator, loop, kwarg, arg, dict, list, tuple, ifelse

### 1. API SEDERHANA

#### branch 02_gethalo

```git
git branch 02_gethalo         # Membuat branch baru
git checkout 02_gethalo       # Berpindah ke branch tersebut
# (lakukan perubahan pada file sesuai kebutuhan)
TAMBAHKAN FILE GIT .gitignore
git add .                       # Menambahkan semua perubahan ke staging area
git commit -m "finish"          # Commit dengan pesan "finish"
git push -u origin 02_gethalo # Push ke remote dan set tracking branch
```

**MEMBUAT API SEDERHANA**

| No  | Method | Endpoint       | Request Body (JSON)                         | Response (JSON)                             |
| --- | ------ | -------------- | ------------------------------------------- | ------------------------------------------- |
| 1   | GET    | `/halo`        | (tidak ada)                                 | `{ "message": "Belajar Flask" }`            |
| 2   | GET    | `/nama/<nama>` | (tidak ada)                                 | `{ "message": "Halo silmi" }`               |
| 3   | POST   | `/halo`        | `{ "nama": "Silmi", "alamat": "Semarang" }` | `{ "nama": "Silmi", "alamat": "Semarang" }` |

- GET HALO

**_LANGKAH : ENVIRONTMENT >> app.py >> test_app.py >> TEST_**

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
pip install flask pytest flask_cors flasgger

#3. app.py
# import >> create object >> route >> funtion return response >> run
#a. import Flask
from flask import Flask, jsonify
#b. create object app
app = Flask(__name__)
#c. create route, method
#### GET, /halo, request:-, response:{ "message": "Belajar Flask" }
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

#### GET, /halo, request:-, response:{ "message": "Belajar Flask" }
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

```git
git branch 03_cleanhalo
git checkout 03_cleanhalo
git push -u origin 03_cleanhalo

git branch 03_cleanhalo         # Membuat branch baru
git checkout 03_cleanhalo       # Berpindah ke branch tersebut
# (lakukan perubahan pada file sesuai kebutuhan)
git add .                       # Menambahkan semua perubahan ke staging area
git commit -m "finish"          # Commit dengan pesan "finish"
git push -u origin 03_cleanhalo # Push ke remote dan set tracking branch
```

**_LANGKAH : docs >> routes >> app.py >> test_app.py >> TEST_**

```
project-folder/
│
├── app.py
├── routes/
│   └── belajar.py
├── docs/
│   └── gethalo.yml
└── test/
    ├──__init__.py
    └── test_belajar.py

```

pada python di wajibkan buat file kosong **init**.py : Tandai folder sebagai package >> Agar bisa di-import sebagai modul

```yml
# Dokumentasi (tag, input, response)
#### tag: Halo, input: -, response: {"message": "Belajar Flask"}
# schema : object >> properties : { key : value(tipe,example) }

# halo.yml
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
          example: Belajar Flask #contoh value object
```

```py
# import >> blouprint >> route >> swagg >> funct resposes
#/routes/belajar.py
from flask import Blueprint, jsonify
from flasgger import swag_from
import os

#'belajar_bp' (param 1)	Nama unik blueprint
# __name__ (param 2)	Nama modul Python → bantu Flask resolve file
belajar_bp = Blueprint('belajar_bp', __name__)

# route, method >> swagger doc >> function return response
#### GET, /halo, request:-, response:{ "message": "Belajar Flask" }
@belajar_bp.route('/halo', methods=['GET'])
@swag_from('../docs/gethalo.yml') #perhatikan script import file (windows, linux, macOS)
def get_halo():
    return jsonify({"message": "Belajar Flask"})
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

#/test/test_belajar.py
# pindahkan test_app.py >> test_belajar.py
# jangan lupa membuat __init__.py (file kosong)
```

Lihat documentation `http://127.0.0.1:5000/apidocs/`

### 3. API SEDERHANA LANJUTAN

#### branch 04_nama

```git
git branch 04_nama         # Membuat branch baru
git checkout 04_nama       # Berpindah ke branch tersebut
# (lakukan perubahan pada file sesuai kebutuhan)
git add .                       # Menambahkan semua perubahan ke staging area
git commit -m "finish"          # Commit dengan pesan "finish"
git push -u origin 04_nama # Push ke remote dan set tracking branch
```

LANGKAH : docs >> belajar.py >> test_belajar.py >> TEST

| No  | Method | Endpoint       | Request Body (JSON) | Response (JSON)               |
| --- | ------ | -------------- | ------------------- | ----------------------------- |
| 2   | GET    | `/nama/<nama>` | (tidak ada)         | `{ "message": "Halo silmi" }` |

```yml
#/docs/nama.yml
# membuat input path, response { "message": "Halo silmi" }
# path : variable name, string, wajib ada, descp
# response : schema: object >> properties : { key : value(tipe,example) }
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

#### branch 05_posthalo

```git
git branch 05_posthalo         # Membuat branch baru
git checkout 05_posthalo       # Berpindah ke branch tersebut
# (lakukan perubahan pada file sesuai kebutuhan)
git add .                       # Menambahkan semua perubahan ke staging area
git commit -m "finish"          # Commit dengan pesan "finish"
git push -u origin 05_posthalo # Push ke remote dan set tracking branch
```

LANGKAH : docs >> belajar.py >> test_belajar.py >> TEST

| No  | Method | Endpoint | Request Body (JSON)                         | Response (JSON)                             |
| --- | ------ | -------- | ------------------------------------------- | ------------------------------------------- |
| 3   | POST   | `/halo`  | `{ "nama": "Silmi", "alamat": "Semarang" }` | `{ "nama": "Silmi", "alamat": "Semarang" }` |

```
METHOD  : POST `/halo`
INPUT   : REQ BODY : `{ "nama": "Silmi", "alamat": "Semarang" }`
PROSES  : -
OUTPUT  : RES BODY : `{ "nama": "Silmi", "alamat": "Semarang" }`
```

```yml
# /docs/posthalo.yml
# Dokumentasi >> tag >> response >> schema >> properties >> {}
# input : body, wajib ada, schema: object >> properties : { key : value(tipe,example) }
# response : schema: object >> properties : { key : value(tipe,example) }
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

```py
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

#tambahkan #/test/test_belajar.py
# function test >> payload ke body >> assert response
def test_post_halo(client):
    payload = {"nama": "Silmi", "alamat": "Semarang"}
    response = client.post('/halo', json=payload)
    assert response.status_code == 200
    assert response.get_json() == payload
```

### 3. CRUD API

#### branch 06_readall

```git
git branch 06_readall         # Membuat branch baru
git checkout 06_readall       # Berpindah ke branch tersebut
# (lakukan perubahan pada file sesuai kebutuhan)
git add .                       # Menambahkan semua perubahan ke staging area
git commit -m "finish"          # Commit dengan pesan "finish"
git push -u origin 06_readall # Push ke remote dan set tracking branch
```

1. MEMBUAT APISPESIFIKASI

| No  | Method | Endpoint      | Request Body (JSON)                                | Response (JSON)                                                                                                       |
| --- | ------ | ------------- | -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 1   | POST   | `/siswa`      | `{ "nama": "Silmi", "alamat": "Semarang" }`        | `{ "message": "Siswa berhasil ditambahkan", "data": { "id": 1, "nama": "Silmi", "alamat": "Semarang" } }`             |
| 2   | GET    | `/siswa`      | (tidak ada)                                        | `{ "message": "Daftar siswa berhasil diambil", "data": [ { "id": 1, "nama": "Silmi", "alamat": "Semarang" }, ... ] }` |
| 3   | GET    | `/siswa/<id>` | (tidak ada)                                        | `{ "message": "Data siswa ditemukan", "data": { "id": 1, "nama": "Silmi", "alamat": "Semarang" } }`                   |
| 4   | PUT    | `/siswa/<id>` | `{ "nama": "Silmi Updated", "alamat": "Jakarta" }` | `{ "message": "Siswa berhasil diperbarui", "data": { "id": 1, "nama": "Silmi Updated", "alamat": "Jakarta" } }`       |
| 5   | DELETE | `/siswa/<id>` | (tidak ada)                                        | `{ "message": "Siswa berhasil dihapus", "data": { "id": 1 } }`                                                        |

Semua respons sukses mengembalikan message dan data: `{ "message": "", "data": {}}`

Untuk error, respons menggunakan: `{ "error": "Pesan error" }`

LANGKAH : docs >> service >> routes >> app.py >> test_siswa.py >> TEST

2. RANCANGAN FOLDER

```
project-folder/
├── app.py
├── routes/
│ ├── siswa.py ← Semua endpoint siswa
│ └── belajar.py
├── docs/ ← Swagger YAML
│ ├── siswa_create.yml
│ ├── siswa_delete.yml
│ ├── siswa_update.yml
│ ├── siswa_read_all.yml ← docs utk read all
│ ├── siswa_read_id.yml
│ ├── nama.yml
│ ├── halo_post.yml
│ └── halo.yml
├── test/
│ ├── **init**.py
│ ├── test_siswa.py ← test untuk siswa api
│ └── test_belajar.py
└── siswa.db ← File SQLite (otomatis dibuat)
```

3. CREATE DATABASE, REGISTER BLUEPRINT

```py
# # # app.py
import sqlite3

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

FUNGSI CURSOR SQL SQLITE LAINNYA

| Fungsi                  | Deskripsi Singkat                                | Return Tipe                     | Kapan Digunakan                                              |
| ----------------------- | ------------------------------------------------ | ------------------------------- | ------------------------------------------------------------ |
| `fetchall()`            | Mengambil semua baris hasil query                | List of tuple/dict              | Jika datanya kecil/sedang dan ingin langsung diproses semua  |
| `fetchone()`            | Mengambil satu baris (per panggilan)             | Tuple/dict                      | Jika hanya butuh 1 baris atau ingin looping manual satu-satu |
| `fetchmany(n)`          | Mengambil `n` baris hasil query                  | List of tuple/dict              | Jika ingin baca data besar secara bertahap                   |
| `lastrowid`             | Mendapatkan ID dari row terakhir yang dimasukkan | Integer                         | Setelah melakukan `INSERT` untuk mendapatkan ID baru         |
| `rowcount`              | Jumlah baris yang terpengaruh query              | Integer                         | Setelah `UPDATE`/`DELETE` untuk tahu berapa baris yang kena  |
| `execute(...)`          | Menjalankan satu query SQL                       | None (hasil disimpan di cursor) | Untuk menjalankan perintah SQL                               |
| `executemany()`         | Menjalankan query berulang dengan banyak data    | None                            | Jika ingin `INSERT` atau `UPDATE` banyak data sekaligus      |
| `connection.commit()`   | Menyimpan perubahan ke database                  | None                            | Setelah `INSERT`, `UPDATE`, `DELETE`                         |
| `connection.rollback()` | Membatalkan perubahan transaksi                  | None                            | Jika terjadi error sebelum `commit()`                        |

PERINTAH SQL PADA PYTHON - SQLITE

```py
with sqlite3.connect('siswa.db') as conn:   # 1 membuat koneksi sql
  cursor = conn.cursor()                    # 2 membuat object cursor
  cursor.execute("SELECT * FROM tb_siswa")  # 3 eksekusi perintah sql
  rows = cursor.fetchall()                  # 4 jika operasi sql dg variabel kembali (rows)
  #conn.commit()                            # 4 jika operasi sql tanpa variabel kembali
```

- READ ALL

1. DEFINISI

API SPESIFICATION

| No  | Method | Endpoint | Request Body (JSON) | Response (JSON)                                                                                                       |
| --- | ------ | -------- | ------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 2   | GET    | `/siswa` | (tidak ada)         | `{ "message": "Daftar siswa berhasil diambil", "data": [ { "id": 1, "nama": "Silmi", "alamat": "Semarang" }, ... ] }` |

SQL QUERY

| METHOD   | PATH/ID | REQ BODY | QUERY SQL                | CURSOR SQL          |
| -------- | ------- | -------- | ------------------------ | ------------------- |
| READ ALL | -       | -        | `SELECT * FROM tb_siswa` | `cursor.fetchall()` |

LANGKAH : docs >> route siswa >> test siswa

2. DOKUMENTASI

```yml
#/docs/siswa_read_all >> response array object >> [{}]
# schema : array >> items :object >> properties {key, value(tipe)}
tags:
  - Siswa
responses:
  200:
    description: Daftar semua siswa
    schema:
      type: object
      properties:
        message:
          type: string
          example: Daftar siswa berhasil diambil
        data:
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
  500:
    description: Gagal mengambil data siswa
    examples:
      application/json:
        error: Gagal mengambil data siswa
```

3. API ROUTE DAN TEST

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

#/test/test_siswa.py
# client >> function test >> get(url) >> assert response
import pytest
from app import app

# membuat object client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_all_siswa(client):
    # method (url)
    response = client.get('/siswa')
    # assert >> code success >> 200
    assert response.status_code == 200
    json_data = response.get_json()

    assert json_data['message'] == "Daftar siswa berhasil diambil"
    # assert >> berupa json >> list
    assert isinstance(json_data['data'], list)

#pytest test\test_siswa.py
```

- READ ALL WITH SERVICES

#### branch 07_readallclean

```git
git branch 07_readallclean         # Membuat branch baru
git checkout 07_readallclean       # Berpindah ke branch tersebut
# (lakukan perubahan pada file sesuai kebutuhan)
git add .                       # Menambahkan semua perubahan ke staging area
git commit -m "finish"          # Commit dengan pesan "finish"
git push -u origin 07_readallclean # Push ke remote dan set tracking branch
```

```
project-folder/
├── app.py
├── routes/
│ ├── siswa.py
│ └── belajar.py
├── services/
│ └── siswa_service.py ← Logika SQL
```

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

```

- CREATE

#### branch 08_create

```
git branch 08_create         # Membuat branch baru
git checkout 08_create       # Berpindah ke branch tersebut
# (lakukan perubahan pada file sesuai kebutuhan)
git add .                       # Menambahkan semua perubahan ke staging area
git commit -m "finish"          # Commit dengan pesan "finish"
git push -u origin 08_create # Push ke remote dan set tracking branch
```

1. DEFINISI

API SPESIFICATION

| No  | Method | Endpoint | Request Body (JSON)                         | Response (JSON)                                                                                           |
| --- | ------ | -------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| 1   | POST   | `/siswa` | `{ "nama": "Silmi", "alamat": "Semarang" }` | `{ "message": "Siswa berhasil ditambahkan", "data": { "id": 1, "nama": "Silmi", "alamat": "Semarang" } }` |

SQL QUERY

| METHOD | PATH/ID | REQ BODY | QUERY SQL                                                                            | CURSOR SQL |
| ------ | ------- | -------- | ------------------------------------------------------------------------------------ | ---------- |
| CREATE | -       | body     | `INSERT INTO tb_siswa (nama, alamat) VALUES (?, ?)` `(data['nama'], data['alamat'])` | -          |

2. DOCUMENTASI

```yml
#request body >> object >> detail object >> response code >> response
#docs/siswa_create.yml
tags:
  - Siswa
summary: Tambah data siswa baru
description: Endpoint untuk menambahkan data siswa ke dalam database.
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
    schema:
      type: object
      properties:
        message:
          type: string
          example: Siswa berhasil ditambahkan
        data:
          type: object
          properties:
            id:
              type: integer
              example: 1
            nama:
              type: string
              example: Budi
            alamat:
              type: string
              example: Jakarta
  400:
    description: Input tidak valid
    examples:
      application/json:
        error: Field 'nama' dan 'alamat' wajib diisi
  500:
    description: Gagal menambahkan siswa
    examples:
      application/json:
        error: Gagal menambahkan siswa
```

3. SERVICE - ROUTE - TEST

```py
#services/siswa_service.py
#...
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


#routes/siswa.py
#...
@siswa_bp.route('/siswa', methods=['POST'])
@swag_from('../docs/siswa_create.yml')
def create_siswa():
    try:
        data = request.get_json()
        # Validasi input sederhana
        if not data or 'nama' not in data or 'alamat' not in data:
            return jsonify({"error": "Field 'nama' dan 'alamat' wajib diisi"}), 400

        siswa_id = siswa_service.create_siswa(data['nama'], data['alamat'])

        return jsonify({
            "message": "Siswa berhasil ditambahkan",
            "data": {
                "id": siswa_id,
                "nama": data['nama'],
                "alamat": data['alamat']
            }
        }), 201

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Gagal menambahkan siswa"}), 500

#test/test_siswa.py
#...
def test_create_siswa(client):
    response = client.post('/siswa', json={"nama": "Silmi", "alamat": "Semarang"})
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data['message'] == "Siswa berhasil ditambahkan"
    assert json_data['data']['nama'] == "Silmi"
    assert json_data['data']['alamat'] == "Semarang"
    assert isinstance(json_data['data']['id'], int)

from unittest.mock import patch

# Test gagal insert karena data kosong atau field tidak lengkap
def test_create_siswa_gagal_validasi(client):
    # data kosong
    response = client.post('/siswa', json={})
    assert response.status_code == 400
    assert response.get_json()['error'] == "Field 'nama' dan 'alamat' wajib diisi"

    # hanya ada nama
    response = client.post('/siswa', json={"nama": "Silmi"})
    assert response.status_code == 400

    # hanya ada alamat
    response = client.post('/siswa', json={"alamat": "Jakarta"})
    assert response.status_code == 400

# Test gagal insert karena terjadi exception di service
def test_create_siswa_gagal_exception(client):
    with patch('services.siswa_service.create_siswa', side_effect=Exception("DB error")):
        response = client.post('/siswa', json={"nama": "Silmi", "alamat": "Semarang"})
        assert response.status_code == 500
        assert response.get_json()['error'] == "Gagal menambahkan siswa"
```

- READ ONE

#### branch 09_readone

```
git branch 09_readone         # Membuat branch baru
git checkout 09_readone       # Berpindah ke branch tersebut
# (lakukan perubahan pada file sesuai kebutuhan)
git add .                       # Menambahkan semua perubahan ke staging area
git commit -m "finish"          # Commit dengan pesan "finish"
git push -u origin 09_readone # Push ke remote dan set tracking branch
```

1. DEFINISI

API SPESIFIKASI

| No  | Method | Endpoint      | Request Body (JSON) | Response (JSON)                                                                                     |
| --- | ------ | ------------- | ------------------- | --------------------------------------------------------------------------------------------------- |
| 3   | GET    | `/siswa/<id>` | (tidak ada)         | `{ "message": "Data siswa ditemukan", "data": { "id": 1, "nama": "Silmi", "alamat": "Semarang" } }` |

SQL QUERY

| METHOD   | PATH/ID | REQ BODY | QUERY SQL                                   | CURSOR SQL          |
| -------- | ------- | -------- | ------------------------------------------- | ------------------- |
| READ ONE | id      | -        | `SELECT * FROM tb_siswa WHERE id=?` `(id,)` | `cursor.fetchone()` |

2. DOKUMENTASI

```yml
#siswa_read_id.yml
tags:
  - Siswa
parameters:
  - name: siswa_id
    in: path
    type: integer
    required: true
    description: ID siswa
responses:
  200:
    description: Detail siswa berdasarkan ID
    examples:
      application/json:
        message: Data siswa ditemukan
        data:
          id: 3
          nama: Coba
          alamat: Bandung
  404:
    description: Siswa tidak ditemukan
    examples:
      application/json:
        error: Siswa dengan ID tersebut tidak ditemukan
  500:
    description: Gagal mengambil data siswa
    examples:
      application/json:
        error: Gagal mengambil data siswa
```

3. SERVICE - ROUTES - TEST

```py
#services/siswa_service.py
#...
def read_siswa_by_id(siswa_id):
    conn = get_db_connection()
    row = conn.execute(
        "SELECT id, nama, alamat FROM tb_siswa WHERE id = ?",
        (siswa_id,)
    ).fetchone()
    conn.close()
    return dict(row) if row else None


#routes/siswa.py
#...
@siswa_bp.route('/siswa/<int:siswa_id>', methods=['GET'])
@swag_from('../docs/siswa_read_id.yml')
def read_siswa_by_id(siswa_id):
    try:
        data = siswa_service.read_siswa_by_id(siswa_id)
        if data:
            return jsonify({
                "message": "Data siswa ditemukan",
                "data": data
            }), 200
        return jsonify({"error": "Siswa dengan ID tersebut tidak ditemukan"}), 404
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Gagal mengambil data siswa"}), 500

#test/test_siswa.py
#...
def test_read_siswa_by_id(client):
    # Tambahkan siswa dulu
    create_response = client.post('/siswa', json={"nama": "Coba", "alamat": "Bandung"})
    siswa_id = create_response.get_json()['data']['id']

    # Baca siswa yang sudah dibuat
    response = client.get(f'/siswa/{siswa_id}')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == "Data siswa ditemukan"
    assert json_data['data']['id'] == siswa_id
    assert json_data['data']['nama'] == "Coba"
    assert json_data['data']['alamat'] == "Bandung"

    # Test siswa yang tidak ada
    response_404 = client.get('/siswa/999999')
    assert response_404.status_code == 404
    assert response_404.get_json()['error'] == "Siswa dengan ID tersebut tidak ditemukan"
```

- DELETE

#### branch 10_delete

```
git branch 10_delete         # Membuat branch baru
git checkout 10_delete       # Berpindah ke branch tersebut
# (lakukan perubahan pada file sesuai kebutuhan)
git add .                       # Menambahkan semua perubahan ke staging area
git commit -m "finish"          # Commit dengan pesan "finish"
git push -u origin 10_delete # Push ke remote dan set tracking branch
```

1. DEFINISI

API SPESIFIKASI

| No  | Method | Endpoint      | Request Body (JSON) | Response (JSON)                                                |
| --- | ------ | ------------- | ------------------- | -------------------------------------------------------------- |
| 5   | DELETE | `/siswa/<id>` | (tidak ada)         | `{ "message": "Siswa berhasil dihapus", "data": { "id": 1 } }` |

SQL QUERY

| METHOD | PATH/ID | REQ BODY | QUERY SQL                                 | CURSOR SQL |
| ------ | ------- | -------- | ----------------------------------------- | ---------- |
| DELETE | id      | -        | `DELETE FROM tb_siswa WHERE id=?` `(id,)` | -          |

2. DOKUMENTASI

```yml
#docs/siswa_delete.yml
tags:
  - Siswa
parameters:
  - name: siswa_id
    in: path
    type: integer
    required: true
    description: ID siswa yang akan dihapus
responses:
  200:
    description: Siswa berhasil dihapus
    examples:
      application/json:
        message: Siswa berhasil dihapus
        data:
          id: 5
  404:
    description: Siswa tidak ditemukan
    examples:
      application/json:
        error: Siswa dengan ID tersebut tidak ditemukan
  500:
    description: Gagal menghapus siswa
    examples:
      application/json:
        error: Gagal menghapus siswa
```

3. SERVICE - ROUTES - TEST

```py
#services/siswa_service.py
#...
def delete_siswa(siswa_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tb_siswa WHERE id = ?", (siswa_id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    return deleted  # 1 jika berhasil dihapus, 0 jika tidak ditemukan


#routes/siswa.py
#...
@siswa_bp.route('/siswa/<int:siswa_id>', methods=['DELETE'])
@swag_from('../docs/siswa_delete.yml')
def delete_siswa(siswa_id):
    try:
        deleted = siswa_service.delete_siswa(siswa_id)
        if deleted:
            return jsonify({
                "message": "Siswa berhasil dihapus",
                "data": {
                    "id": siswa_id
                }
            }), 200
        return jsonify({"error": "Siswa dengan ID tersebut tidak ditemukan"}), 404
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Gagal menghapus siswa"}), 500


#test/test_siswa.py
#...
def test_delete_siswa(client):
    # Tambahkan siswa terlebih dahulu
    create_response = client.post('/siswa', json={"nama": "Delete Me", "alamat": "Nowhere"})
    siswa_id = create_response.get_json()['data']['id']

    # Lakukan DELETE
    response = client.delete(f'/siswa/{siswa_id}')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == "Siswa berhasil dihapus"
    assert json_data['data']['id'] == siswa_id

    # DELETE lagi → harusnya 404
    response_2 = client.delete(f'/siswa/{siswa_id}')
    assert response_2.status_code == 404
    assert response_2.get_json()['error'] == "Siswa dengan ID tersebut tidak ditemukan"

```

- UPDATE

#### branch 11_update

```
git branch 11_update         # Membuat branch baru
git checkout 11_update       # Berpindah ke branch tersebut
# (lakukan perubahan pada file sesuai kebutuhan)
git add .                       # Menambahkan semua perubahan ke staging area
git commit -m "finish"          # Commit dengan pesan "finish"
git push -u origin 11_update # Push ke remote dan set tracking branch
```

1. DEFINISI

API SPESIFIKASI

| No  | Method | Endpoint      | Request Body (JSON)                                | Response (JSON)                                                                                                 |
| --- | ------ | ------------- | -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| 4   | PUT    | `/siswa/<id>` | `{ "nama": "Silmi Updated", "alamat": "Jakarta" }` | `{ "message": "Siswa berhasil diperbarui", "data": { "id": 1, "nama": "Silmi Updated", "alamat": "Jakarta" } }` |

SQL QUERY

| METHOD | PATH/ID | REQ BODY | QUERY SQL                                                                              | CURSOR SQL |
| ------ | ------- | -------- | -------------------------------------------------------------------------------------- | ---------- |
| UPDATE | id      | body     | `UPDATE tb_siswa SET nama=?, alamat=? WHERE id=?` `(data['nama'], data['alamat'], id)` | -          |

2. DOKUMENTASI

```yml
#docs/siswa_update.yml
tags:
  - Siswa
summary: Perbarui data siswa berdasarkan ID
description: Endpoint untuk memperbarui nama dan alamat siswa berdasarkan ID.
parameters:
  - name: siswa_id
    in: path
    required: true
    type: integer
    description: ID siswa yang akan diperbarui
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
          example: Budi Updated
        alamat:
          type: string
          example: Surabaya
responses:
  200:
    description: Siswa berhasil diperbarui
    schema:
      type: object
      properties:
        message:
          type: string
          example: Siswa berhasil diperbarui
        data:
          type: object
          properties:
            id:
              type: integer
              example: 1
            nama:
              type: string
              example: Budi Updated
            alamat:
              type: string
              example: Surabaya
  400:
    description: Field wajib tidak diisi
    examples:
      application/json:
        error: Field 'nama' dan 'alamat' wajib diisi
  404:
    description: Siswa tidak ditemukan
    examples:
      application/json:
        error: Siswa tidak ditemukan
  500:
    description: Gagal memperbarui siswa
    examples:
      application/json:
        error: Gagal memperbarui siswa
```

3. SERVICE - ROUTES - TEST

```py
#services/siswa_service.py
#...
def update_siswa(siswa_id, nama, alamat):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tb_siswa SET nama = ?, alamat = ? WHERE id = ?",
        (nama, alamat, siswa_id)
    )
    conn.commit()
    updated = cursor.rowcount  # Mengecek apakah baris ter-update
    conn.close()
    return updated  # 0 jika tidak ada yang diupdate, 1 jika berhasil


#routes/siswa.py
#...
@siswa_bp.route('/siswa/<int:siswa_id>', methods=['PUT'])
@swag_from('../docs/siswa_update.yml')
def update_siswa(siswa_id):
    try:
        data = request.get_json()

        # Validasi input
        if not data or 'nama' not in data or 'alamat' not in data:
            return jsonify({"error": "Field 'nama' dan 'alamat' wajib diisi"}), 400

        updated = siswa_service.update_siswa(siswa_id, data['nama'], data['alamat'])

        if updated == 0:
            return jsonify({"error": "Siswa dengan ID tersebut tidak ditemukan"}), 404

        return jsonify({
            "message": "Siswa berhasil diperbarui",
            "data": {
                "id": siswa_id,
                "nama": data['nama'],
                "alamat": data['alamat']
            }
        }), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Gagal memperbarui siswa"}), 500


#test/test_siswa.py
#...
def test_update_siswa(client):
    # Tambah siswa dulu agar bisa diupdate
    create_response = client.post('/siswa', json={"nama": "Ani", "alamat": "Solo"})
    siswa_id = create_response.get_json()['data']['id']

    # Update siswa
    response = client.put(f'/siswa/{siswa_id}', json={"nama": "Ani Updated", "alamat": "Semarang"})
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == "Siswa berhasil diperbarui"
    assert json_data['data']['id'] == siswa_id
    assert json_data['data']['nama'] == "Ani Updated"
    assert json_data['data']['alamat'] == "Semarang"

```

### 5. AUTH API

#### branch 12_register

```
git branch 12_register         # Membuat branch baru
git checkout 12_register       # Berpindah ke branch tersebut
# (lakukan perubahan pada file sesuai kebutuhan)
git add .                       # Menambahkan semua perubahan ke staging area
git commit -m "finish"          # Commit dengan pesan "finish"
git push -u origin 12_register # Push ke remote dan set tracking branch
```


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


1. DEFINISI

API SPESIFIKASI

SQL QUERY

2. DOKUMENTASI

```yml
#auth/register.yml
tags:
  - Auth
summary: Registrasi akun baru
description: Endpoint untuk mendaftarkan akun pengguna baru.
consumes:
  - application/json
produces:
  - application/json
parameters:
  - in: body
    name: body
    required: true
    description: Data user baru
    schema:
      type: object
      required:
        - username
        - password
      properties:
        username:
          type: string
          example: johndoe
        password:
          type: string
          example: rahasia123
responses:
  201:
    description: Registrasi berhasil
    schema:
      type: object
      properties:
        message:
          type: string
          example: Registrasi berhasil
  400:
    description: Input tidak lengkap
    schema:
      type: object
      properties:
        error:
          type: string
          example: Field 'username' dan 'password' wajib diisi
  409:
    description: Username sudah digunakan
    schema:
      type: object
      properties:
        error:
          type: string
          example: Username sudah digunakan
```

3. SERVICE - ROUTES - TEST

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


def test_register_success(client):
    response = client.post('/register', json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 201
    assert response.get_json()["message"] == "Registrasi berhasil"

def test_register_duplicate(client):
    # Register pertama kali
    client.post('/register', json={
        "username": "testuser",
        "password": "testpass"
    })

    # Register ulang dengan username yang sama
    response = client.post('/register', json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 409
    assert response.get_json()["error"] == "Username sudah digunakan"

def test_register_missing_fields(client):
    response = client.post('/register', json={
        "username": "incomplete"
        # password tidak dikirim
    })
    assert response.status_code == 400
    assert "wajib diisi" in response.get_json()["error"]

#pytest test/test_auth.py
```

- LOGIN

#### branch 13_login

```
git branch 13_login         # Membuat branch baru
git checkout 13_login       # Berpindah ke branch tersebut
# (lakukan perubahan pada file sesuai kebutuhan)
git add .                       # Menambahkan semua perubahan ke staging area
git commit -m "finish"          # Commit dengan pesan "finish"
git push -u origin 13_login # Push ke remote dan set tracking branch
```

1. DEFINISI

API SPESIFIKASI

SQL QUERY

2. DOKUMENTASI

```yml
#auth/login.yml
tags:
  - Auth
summary: Login pengguna
description: Endpoint untuk login dan mendapatkan token autentikasi.
consumes:
  - application/json
produces:
  - application/json
parameters:
  - in: body
    name: body
    required: true
    description: Data login pengguna
    schema:
      type: object
      required:
        - username
        - password
      properties:
        username:
          type: string
          example: johndoe
        password:
          type: string
          example: rahasia123
responses:
  200:
    description: Login berhasil
    schema:
      type: object
      properties:
        message:
          type: string
          example: Login berhasil
        token:
          type: string
          example: 4a1f70de-5d72-48ac-9187-01d3b7c177dd
  400:
    description: Input tidak lengkap
    schema:
      type: object
      properties:
        error:
          type: string
          example: Field "username" dan "password" wajib diisi
  401:
    description: Login gagal
    schema:
      type: object
      properties:
        error:
          type: string
          example: Username atau password salah
```

3. SERVICE - ROUTES - TEST

```py
#1. Folder routes/auth.py
#..................
@auth_bp.route('/login', methods=['POST'])
@swag_from('../docs/auth/login.yml')
def login():
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
      return jsonify({'error': 'Field "username" dan "password" wajib diisi'}), 400

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

def test_login_wrong_password(client):
    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'salahpass'
    })
    assert response.status_code == 401
    assert response.get_json()['error'] == 'Username atau password salah'

def test_login_user_not_found(client):
    response = client.post('/login', json={
        'username': 'nouser',
        'password': 'whatever'
    })
    assert response.status_code == 401
    assert response.get_json()['error'] == 'Username atau password salah'

def test_login_missing_fields(client):
    response = client.post('/login', json={
        'username': 'testuser'
        # password tidak dikirim
    })
    assert response.status_code == 400
    assert 'wajib diisi' in response.get_json()['error']
```

- LOGOUT

#### branch 14_logout

```
git branch 14_logout         # Membuat branch baru
git checkout 14_logout       # Berpindah ke branch tersebut
# (lakukan perubahan pada file sesuai kebutuhan)
git add .                       # Menambahkan semua perubahan ke staging area
git commit -m "finish"          # Commit dengan pesan "finish"
git push -u origin 14_logout # Push ke remote dan set tracking branch
```

1. DEFINISI

API SPESIFIKASI

SQL QUERY

2. DOKUMENTASI

```yml
#auth/logout.yml
tags:
  - Auth
summary: Logout pengguna
description: Endpoint untuk logout dengan menghapus token autentikasi.
consumes:
  - application/json
produces:
  - application/json
parameters:
  - in: header
    name: Authorization
    required: true
    type: string
    description: Token autentikasi pengguna
    example: 4a1f70de-5d72-48ac-9187-01d3b7c177dd
responses:
  200:
    description: Logout berhasil
    schema:
      type: object
      properties:
        message:
          type: string
          example: Logout berhasil
  401:
    description: Token tidak valid atau tidak ada
    schema:
      type: object
      properties:
        error:
          type: string
          example: Token tidak valid
```

3. SERVICE - ROUTES - TEST

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

def test_logout_missing_token(client):
    response = client.post('/logout')
    assert response.status_code == 401
    assert response.get_json()['error'] == 'Token tidak ditemukan'

def test_logout_invalid_token(client):
    response = client.post('/logout', headers={
        'Authorization': 'invalid-token-xyz'
    })
    assert response.status_code == 401
    assert response.get_json()['error'] == 'Token tidak valid'
```

### 5. AUTH API CRUD SISWA

- CRUD

#### branch 15_crudauth

```
git branch 15_crudauth         # Membuat branch baru
git checkout 15_crudauth       # Berpindah ke branch tersebut
# (lakukan perubahan pada file sesuai kebutuhan)
git add .                       # Menambahkan semua perubahan ke staging area
git commit -m "finish"          # Commit dengan pesan "finish"
git push -u origin 15_crudauth # Push ke remote dan set tracking branch
```

1. DEFINISI

API SPESIFIKASI

2. DOKUMENTASI

3. SERVICE - ROUTES - TEST

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

```
git branch 16_testcrud         # Membuat branch baru
git checkout 16_testcrud       # Berpindah ke branch tersebut
# (lakukan perubahan pada file sesuai kebutuhan)
git add .                       # Menambahkan semua perubahan ke staging area
git commit -m "finish"          # Commit dengan pesan "finish"
git push -u origin 16_testcrud # Push ke remote dan set tracking branch
```

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

```
git branch 17_docker         # Membuat branch baru
git checkout 17_docker       # Berpindah ke branch tersebut
# (lakukan perubahan pada file sesuai kebutuhan)
git add .                       # Menambahkan semua perubahan ke staging area
git commit -m "finish"          # Commit dengan pesan "finish"
git push -u origin 17_docker # Push ke remote dan set tracking branch
```

### 7. GUNAKAN DATABASE POSTGREE > DOCKER

#### branch 18_postgre

```
git branch 18_postgre         # Membuat branch baru
git checkout 18_postgre       # Berpindah ke branch tersebut
# (lakukan perubahan pada file sesuai kebutuhan)
git add .                       # Menambahkan semua perubahan ke staging area
git commit -m "finish"          # Commit dengan pesan "finish"
git push -u origin 18_postgre # Push ke remote dan set tracking branch
```
