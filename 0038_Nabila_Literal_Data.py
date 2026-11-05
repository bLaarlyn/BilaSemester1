# membuat daftar nama variabel beserta tipe data
data_string = "Nabila Arlyn Alva Rianna"
data_integer = 18
data_float = 49.3

print("Nama : ", data_string)
print("Umur : ", data_integer)
print("Berat Badan : ", data_float)

# konversi tipe data
angka_string = "123"
angka_int = int(angka_string) #konversi data ke integer
print("string ke integer : ", angka_int, ", type : ", type(angka_int))

angka_float = 45.67
angka_int = int(angka_float) # konversi data ke integer
print("float ke integer : ", angka_int, ", type : ", type(angka_int))

angka_integer = 89 
angka_float = float(angka_integer) # konversi data ke float
angka_str = str(angka_integer) # konversi data ke string
print("integer ke float : ", angka_float, ", type : ", type(angka_float))
print("integer ke string : ", angka_str, ", type : ", type(angka_str))

# membuat program input 
usia = int (input("Masukkan usia : "))
tinggi_badan = float (input("Masukkan Tinggi Badan : "))
nama = input("Masukkan Nama : ")

print("Usia : ", usia, ", type : ", type(usia))
print("Tinggi Badan : ", tinggi_badan, ", type : ", type(tinggi_badan))
print("Nama : ", nama, ", type : ", type(nama))
