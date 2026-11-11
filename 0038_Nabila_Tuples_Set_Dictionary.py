#program 10.1 Tuples dan sets
# kalau LIST menggunakan kurung siku
#tuples
data_tuples = (7, 8, 10, 11)
print(data_tuples)
print(data_tuples[1])
#sets (himpunan)
data_sets = (10, 4, 3, 2, 7, 6, 5)
print(data_sets)

print(data_sets[0])

#program 10.2 Dictionary
data_bb = ['Arlyn', 38, 'Teknologi informasi', 161, 18]
data_mahasiswa = {
    'Nama': 'Arlyn',
    'NIM' : 38,
    'prodi' : 'Teknologi informasi',
    'Tinggi' : 161,
    'usia' : 18,
    'List' : data_bb
}
print(data_mahasiswa['Nama'])
print(data_mahasiswa['NIM'])
print(data_mahasiswa['List'])

#Program 10.3 Operasi Dictionary
data_orang = {
    "Nama" : "Alva",
    "NIM" : 2605,
    "prodi" : "teknologi informasi"
}

# panjang dictionary
LENDICT = len(data_orang)
print(f"panjang dictionary :{LENDICT}")
# mengecek key exist atau tidak
KEY = "Nama"
CHECKKEY = KEY in data_orang
print(f"apakah {KEY} ada di data_orang: {CHECKKEY}")
#mengakses value (read) dengan get
print(data_orang["Nama"])
print(data_orang.get("Nama"))
print(data_orang.get("Tinggi","key tidak ditemukan"))
#mengupdate data
data_orang["Nama"] = "okkey"
print(data_orang)
data_orang["lyn"] = "siap"
print(data_orang)

data_orang.update({"Nama": "Arlyn"})
print(data_orang)
data_orang.update({"bb":49})
print(data_orang)
#menghapus data
del data_orang["bb"]
print(data_orang)
#program 10.4 Looping Dictionary
mhs_mahasiswa = {
    "Nama":"Arlyn baik",
    "prodi":"Teknologi Informasi",
    "kampus":"tuguran"
}
#looping first try yang keluar hanya key
for mahasiswa in mhs_mahasiswa:
    print(mahasiswa)
#operator untuk mengambil item
keys = mhs_mahasiswa.keys()
print(keys)

for key in mhs_mahasiswa.keys():
    print(mhs_mahasiswa.get(key))

values = mhs_mahasiswa.values()
print(values)

for value in mhs_mahasiswa.values():
    print(value)

items = mhs_mahasiswa.items()
print(items)

for item in mhs_mahasiswa.items():
    print(item)
for key,value in mhs_mahasiswa.items():
    print(f"key = {key}, value = {value}")

print("===LATIHAN NOMOR 1 (TUPLE)====")
data_mahasiswa = ("Alva", "2605060038", "Teknologi informasi")
print(data_mahasiswa[1])
print(data_mahasiswa[2])
# mahasiswa[2] = "Teknologi informasi"
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print(nilai_angka)

print("===LATIHAN NOMOR 2 (MANIPULASI DICTIONARY)")
data_mahasiswa ={
    "nim":"240101",
    "nama":"Budi Santoso",
    "prodi":"Teknologi Informasi"
}
data_mahasiswa["prodi"] = "Sastra Mesin"
data_mahasiswa["angkatan"] = "2026"
del data_mahasiswa["nim"]
print(data_mahasiswa)

print("===LATIHAN NOMOR 3(PERULANGAN PADA DICTIONARY)")
keranjang = {
    "apel":5000,
    "pisang":3000,
    "jeruk":7000,
    "anggur":15000
}
total_belanja=0

for buah,harga in keranjang.items():
    print(f"Harga {buah}: {harga}")
    total_belanja += harga
print(f"Total belanjanya adalah: {total_belanja}")
