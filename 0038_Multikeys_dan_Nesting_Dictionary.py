# # #PROGRAM11.1 MULTI KEYS DAN NESTING DICTIONARY
# import datetime
# mahasiswa1 = {
#     'nama':'Ucup surucup',
#     'nim':'19022001',
#     'sks_lulus':130,
#     'beasiswa':False,
#     'Lahir':datetime.datetime(2001,4,10)
# }

# mahasiswa2 = {
#     'nama':'Azan maghrib',
#     'nim':'19022002',
#     'sks_lulus':140,
#     'beasiswa':True,
#     'Lahir':datetime.datetime(2002,10,10)
# }

# mahasiswa3 = {
#     'nama':'slamet Dunia Akhirat',
#     'nim':'19022003',
#     'sks_lulus':100,
#     'beasiswa':True,
#     'Lahir':datetime.datetime(1977,5,10)
# }

# data_mahasiswa = {
#     'MAH001':mahasiswa1,
#     'MAH002':mahasiswa2,
#     'MAH003':mahasiswa3
# }

# print(f"{'KEY':<6} {'NAMA':<6} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
# print("_"*50)

# for mahasiswa in data_mahasiswa:
#     KEY = mahasiswa
#     NAMA = data_mahasiswa[KEY]['nama']
#     NIM = data_mahasiswa[KEY]['nim']
#     SKS = data_mahasiswa[KEY]['sks_lulus']
#     BEASISWA = data_mahasiswa[KEY]['beasiswa']
#     LAHIR = data_mahasiswa[KEY]['Lahir'].strftime("%x")

#     print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:<9} {LAHIR:<10}")

# # #PROGRAM 11.2 LATIHAN DICTIONARY BAGIAN 1
# import datetime
# mahasiswa_template = {
#     'nama':'nama',
#     'nim':00000000,
#     'sks_lulus':0,
#     'Lahir':datetime.datetime(1111,1,11)
# }
# data_mahasiswa = {}
# print(f"{'SELAMAT DATANG':^20}")
# print(f"{'DATA MAHASISWA':^20}")
# print("-"*20)

# mahasiswa = dict.fromkeys(mahasiswa_template.keys())
# print(mahasiswa)
# mahasiswa['nama'] = input("Nama Mahasiswa:")
# mahasiswa['nim'] = input("NIM Mahasiswa: ")
# mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
# TAHUN_LAHIR = int(input("Tahun lahir (yyyy) :"))
# BULAN_LAHIR = int(input("Bulan lahir (1-12) :"))
# TANGGAL_LAHIR = int(input("Tanggal lahir (1-31)"))
# mahasiswa['Lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

# print(mahasiswa)

# # #PROGRAM 11.3 LATIHAN DICTIONARY BAGIAN 2
# import datetime
# import os
# import string
# import random

# mahasiswa_template = {
#     'nama':'nama',
#     'nim':00000000,
#     'sks_lulus':0,
#     'lahir':datetime.datetime(1111,1,11)
# }

# data_mahasiswa = {}

# while True:
#     os.system("clear")
#     print(f"{'SELAMAT DATANG':^20}")
#     print(f"{'DATA MAHASISWA':^20}")
#     print("-"*20)

#     mahasiswa = dict.fromkeys(mahasiswa_template.keys())
#     mahasiswa['nama'] = input("Nama Mahasiswa:")
#     mahasiswa['nim'] = input("NIM Mahasiswa: ")
#     mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
#     TAHUN_LAHIR = int(input("Tahun lahir (yyyy) :"))
#     BULAN_LAHIR = int(input("Bulan lahir (1-12) :"))
#     TANGGAL_LAHIR = int(input("Tanggal lahir (1-31)"))
#     mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

#     KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
#     data_mahasiswa.update({KEY:mahasiswa})

#     #dari program sebelumnya, hilangkan beasiswa
#     print(f"\n{'KEY':<6} {'Nama' :<17} {'NIM':<14} {'SKS Lulus':<10} {'Tanggal Lahir':<10}")
#     print('_'*60)

#     for mahasiswa in data_mahasiswa:
#         KEY = mahasiswa
#         NAMA = data_mahasiswa[KEY]['nama']
#         NIM = data_mahasiswa[KEY]['nim']
#         SKS = data_mahasiswa[KEY]['sks_lulus']
#         LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

#         print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")

#     print("\n")
#     is_done = input("Mau tambah lagi bro (y/n)? ")
#     if is_done == "n":
#         break

# print("\n Akhir dari program, thank you") 

print('===SISTEM MANAJEMEN PERPUSTAKAAN===')

import datetime
import os
import string
import random

sistem_perpustakaan = {
    'judul':'judul',
    'penulis':'penulis',
    'tahun terbit':0000,
    'tanggal terakhir pinjam':datetime.datetime(1111,1,11),
    'status': 'ada/tidak'
}

data_buku = {}
while True:
    os.system("cls")
    print(f"{'SELAMAT DATANG':^90}")
    print(f"{'SISTEM MANAJEMEN PERPUSTAKAAN':^90}")
    print("-"*105)

    buku = dict.fromkeys(sistem_perpustakaan.keys())
    buku['judul'] = input("Judul Buku: ")
    buku['penulis'] = input("Nama penulis: ")
    buku['tahun terbit'] = int(input("Tahun buku terbit: "))
    TAHUN = int(input("Tahun terakhir pinjam: "))
    BULAN = int(input("Bulan teraakhir pinjam: "))
    TANGGAL = int(input("Tanggal terakhir pinjam: "))
    buku['tanggal terakhir pinjam'] = datetime.datetime(TAHUN,BULAN,TANGGAL)
    buku['status'] = input("Status buku (ada/tidak): ")
    KEYS =''.join(random.choice(string.ascii_uppercase) for i in range(6))

    data_buku[KEYS] = buku
    print(f"{'DATA BUKU DI PERPUSTAKAAN':^90}")
    print("-"*105)
    print(f"\n{'KEYS':<8} {'judul':<30} {'penulis':<15} {'tahun terbit':<15} {'tanggal terakhir pinjam':<25} {'status':<10}")
    print("-"*105)

    for buku in data_buku: 
        KEYS = buku
        JUDUL = data_buku[KEYS]['judul']
        PENULIS = data_buku[KEYS]['penulis']
        TAHUNTERBIT = data_buku[KEYS]['tahun terbit']
        TANGGALTERAKHIRPINJAM = data_buku[KEYS]['tanggal terakhir pinjam'].strftime("%x")
        STATUS = data_buku[KEYS]['status']

        print(f"{KEYS:<8} {JUDUL:<30} {PENULIS:<15} {TAHUNTERBIT:<15} {TANGGALTERAKHIRPINJAM:<25} {STATUS:<10} ")

    print("\n")
    is_done = input("Mau pinjam buku lagi (y/n)? ")

    if is_done == "n":
        break
print("\n Akhir dari program, thank you")