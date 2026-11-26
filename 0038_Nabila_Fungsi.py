# program 12.1 membuat fungsi
def hello_world():
    print("hello world")
    print("kepada fauzan zein")
    print("dan juga kepada faza biri biri")

hello_world()

#program 12.2 funhsi dengan argumen
def say_hello(nama):
    print(f"hello{nama}")
say_hello("Nabila")

def tambah(angka_1, angka_2):
    hasil = angka_1+angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")
tambah(2,7)

def say_hi(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"selamat datang{peserta}")

kumpulan_mahasiswa = ["Alva", "Arlyn", "Anna"]
say_hi(kumpulan_mahasiswa)

# program 12.3 fungsi dan return
def kuadrat(input_angka):
    output_kuadrat = input_angka ** 2
    return output_kuadrat
y = kuadrat(5)
print(y)
print(kuadrat(6))
z = 10 + kuadrat(7)
print(z)

def fungsi_tambah(angka_1, angka_2):
    return angka_1+angka_2
a = fungsi_tambah(10,8)
print(a)

def operasi_matematika(angka_1, angka_2):
    tambah = angka_1+angka_2
    kurang = angka_1-angka_2
    kali = angka_1*angka_2
    bagi = angka_1/angka_2
    return tambah, kurang, kali, bagi

k,l,m,n = operasi_matematika(9,5)
print(f"hasil tambah = {k}")
print(f"hasil kurang = {l}")
print(f"hasil kali = {m}")
print(f"hasil bagi = {n}")

# program 12.4 default argumen fungsi
def say_hello(nama = "tina "):
    print(f"Hello {nama}")
say_hello("Bila")
say_hello()

def sapa_dia(nama, pesan = "Apa kabar?"):
    print(f"hai {nama}, {pesan}")
sapa_dia("Nanda", "Bonjour")
sapa_dia("Madame")

def hitung_pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil
print(hitung_pangkat(2,4))
hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil)

def faktorial(input_1=1, input_2=2, input_3=3, input_4=4):
    hasil = input_1*input_2*input_3*input_4
    return hasil
print(faktorial())
print(faktorial(input_3 = 10))

print("====LATIHAN FUNGSI====")
print("1. menghitung luas persegi panjang")
def luas_persegipanjang(panjang, lebar):
    hasil = panjang*lebar
    return hasil
panjang = float(input("panjangnya: "))
lebar = float(input("Lebarnya: "))
hasil = luas_persegipanjang(panjang, lebar)
print(f"Luas persegi panjang = {hasil}")

print("2. menghitung volume persegi panjang")
def volume_persegipanjang(panjang, lebar, tinggi):
    hasil = panjang*lebar*tinggi
    return hasil
panjang = float(input("panjangnya: "))
lebar = float(input("lebarnya: "))
tinggi = float(input("tingginya: "))
hasil = volume_persegipanjang(panjang, lebar, tinggi)
print(f"Volume persegi panjang = {hasil}")

print("3.menghitung luas lingkaran")
def luas_lingkaran(jarijari):
    hasil = 3.14*jarijari**2
    return hasil
jarijari = float(input("Jari-jarinya: "))
hasil = luas_lingkaran(jarijari)
print(f"Luas LIngkaran = {hasil}")

print("4.menghitung volume bola")
def volume_bola(jari2):
    hasil = (4/3)*3.14*jari2**3
    return hasil
jari2 = float(input("jari-jari: "))
hasil = volume_bola(jari2)
print(f"Volume bola = {hasil}")