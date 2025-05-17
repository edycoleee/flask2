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
