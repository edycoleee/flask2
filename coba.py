# 1. DECORATOR
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
    print("DECORATOR : Halo Function")

#say_hello()

# 2. Decorator dengan Parameter
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def halo():
    print("DECORATOE PARAM : Halo!")

#halo()

# 3. LOOPING dengan tanda _
def functloop(x):
    for _ in range(x):
        print("LOOP : Halo Silmi")

#functloop(5)

# 4 **kwarg
def halokwarg(**kwargs):
    print("KWARGS : ", kwargs)
#halokwarg(nama="silmi", usia=12)

# 5 **arg
def haloarg(*args):
    print("ARGS : ", args)
#haloarg(1,2,3,4)

# 6 DICT {}
user = {
    "nama": "Andi",
    "usia": 25
}
print("DICT : ", user["nama"])  # Output: Andi

# 7 LIST ()
lokasi = ("Jakarta", -6.2)
print("LIST : ",lokasi[0])  # Output: Jakarta

# 8 TUPLE []
def namabuah(buah):
    print("TUPLE : ", buah)

buah = ["apel", "jeruk", "pisang"]
namabuah(buah)
buah[0] = "mangga"           # Bisa diubah
namabuah(buah)
buah.append("anggur")        # Bisa ditambah
namabuah(buah)

# 9 IF ELSE
def cekdewasa(x):
    if x>17 :
        print("Dewasa")
    else:
        print("Belum Dewasa")

cekdewasa(18)
