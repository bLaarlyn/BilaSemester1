# program 9.1 List
# Kumpulan data numbers
data_angka = [1, 5, 2, 3]
print(data_angka)
# kumpulan data string
data_string =["ucup","adit","siti"]
print(data_string)
#kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)
#Kumpulan campuran
data_campuran = [1,"bakwan", 2,"cireng", "ucup", True,"adit",False]
print(data_campuran)
#cara alternatif buat list
data_range = range(0, 10, 2) # range (start, step, stop)
print(data_range)
data_list = list(data_range)
print(data_list)
#mmebuat list dengan for loop, list comprehension
list_for = [i **2 for i in range(0,10)]
print(list_for)
# membuat list pake for pake if
list_for_if = [i for i in range(0,10) if i !=5]
print(list_for_if)
list_for_if = [i for i in range(0,10) if i %2 == 0]
print(list_for_if)
list_for_if = [i for i in range(0,10) if i %2 !=0]
print(list_for_if)
# program 9.2 Manipulasi List
# index 0(-3) 1(-2) 2(-1)
data = ["ucup", "Adit", "Dudung"]
#menganbil data dari list
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")
data_akhir = data[-1]
print(f"data terakhir adalah = {data_akhir}")
#mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")
# manipulasi data list
# menambahkan item pada list sesuai posisi
print(f"data sebeleum ditambah = \n{data}")
#data.insert(posisi,item)
data.insert(1, "Asep")
print(f"data sesudah ditambah= \n{data}")
#menambah diakhir list
data.append("Ririn")
print(f"data ditambah lagi = \n{data}")
#menambahkan list dengan list
data_baru = ["Lala","Zaza","Nana"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")
#merubah data
data[2] = "jaja"
print(f"data rubah = \n{data}")
#menghapus data
data.remove("Nana")
print(f"data hapus = \n{data}")
#menghapus data paling belakang
data.pop()
print(f"data akhir = \n{data}")
#Program 9.3 Operasi List
data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]
print(f"data angka =\n{data_angka}")
#count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

#ambil posisi data
data = ["Arsyi", "Nabila", "Arin", "Mutiara"]
print(f"data = {data}")
index_Nabila = data.index("Nabila")
index_Arin = data.index("Arin")
print(f"index si Nabila = {index_Nabila}")
print(f"index si Arin = {index_Arin}")

#Mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")
#balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse \n{data_angka}")
print(f"data di reverse \n{data}")

#program 9.4 Nested LIst
data_0 = [1,2]
data_1 = [3, 4]
data_list_biasa = [1, 2, 3, 4]
print(f"list  biasa = {data_list_biasa}")

list_2D = [data_0, data_1, 6, 7]
print(f"list 2D = {list_2D}")
#penggunaaan
peserta_0 = ["Arlyn", 18, "Perempuan"]
peserta_1 = ["Alva", 16, "Laki-laki"]
peserta_2 = ["Rianna", 20, "Perempuan"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"nama\t : {peserta[0]}")
    print(f"umur\t : {peserta[1]}")
    print(f"Gender\t : {peserta[2]}\n")
      
print ("LATIHAN NOMOR 1")
kendaraan = ["Motor", "Mobil", "Sepeda", "Bus"]
# menambah truk diakhir list
kendaraan.append("Truk")
print(f"data ditambah lagi= \n{kendaraan}")
# becak pada indeks 1
kendaraan.insert(1,"Becak")
print(f"data sesudah ditambah= \n{kendaraan}")
# hapus data paling terakhr
kendaraan.pop()
print(f"data akhir = \n{kendaraan}")
# sepeda menjadi skuter
kendaraan [3] = "Skuter"
print(f"data rubah = \n{kendaraan}")
#jumlah total data di dalam list
jumlah_data = len(kendaraan)
print (f"jumlah total kendaraan = \n{kendaraan}")

print ("LATIHAN NOMOR 2")
angka = [75, 80, 90, 75, 85, 100, 65]
#indeks keberapa 100
print(f"data = {angka}")
index_100 = angka.index(100)
print(f"index angka 100 = {index_100}")
#berapa siswa mendapat 75
jumlah_nilai_75 = angka.count(75)
print(f"jumlah yang mendapat nilai 75 yaitu: {jumlah_nilai_75}")
#urutkan dari kecil hingga besar
angka.sort()
print(f"Angka dari kecil ke besar = {angka}")
#balikkan urutan list dari besar ke kcil
angka.reverse()
print(f"angka setelah dibalikkan urutannya = {angka}")

print ("LATIHAN NOMOR 3")
menu_utama = ["Nasi Goreng", "Mie ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]

menu_utama.extend(menu_tambahan)
print(f"{menu_utama}")

print ("LATIHAN NOMOR 4")
data_barang = [["BUku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]
# menampilkan harga pensil dengan memanggil indeks
harga_pensil = data_barang[1][1]
print(f"harga pensil= {harga_pensil}")
#Perulangan satu persatu
for barang in data_barang:
    print(f"nama barang\t : {barang[0]}")
    print(f"harga barang\t :{barang[1]}")
