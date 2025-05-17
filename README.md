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
