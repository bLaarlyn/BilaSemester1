# PERCOBAAN PROGRAM 3.1
# operasi aritmatika
a = 10
b = 3

# operasi tambah +
hasil = a + b
print (a,'+',b,'=',hasil)

# operasi kurang -
hasil = a - b
print (a,'-',b,'=',hasil)

# operasi perkalian *
hasil = a*b
print (a,'*',b,'=',hasil)

# operasi pembagian /
hasil = a/b
print (a, '/',b,'=',hasil)

# operasi eksponen (pangkat) **
hasil = a**b
print (a,'**',b,'=',hasil)

# operasi modulus %
hasil = a%b
print (a,'%',b,'=',hasil)

# operasi floor division //
hasil = a//b
print (a,'//',b,'=',hasil)

# PERCOBAAN PROGRAM 3.2
# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")
celcius = float(input('Masukkan suhu dalam celcius : '))
print("suhu adalah", celcius, "Celcius")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah", reamur, "Reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah", fahrenheit, "Fahrenheit")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah", kelvin, "Kelvin")

# PERCOBAAN PROGRAM 3.3
# operasi komperasi yang setiap hasilnya adalah Boolean
# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# lebih besar dari >
print("=============== lebih besar dari (>)")
hasil = a > 3
print(a, '>',b,'=',hasil)
hasil = b > 3
print(b, '>',3, '=',hasil)
hasil = b > 2
print(b, '>',2, '=', hasil)

# kurang dari <
print("=============== kurang dari (<)")
hasil = a < 3
print(a, '<',3, '=',hasil)
hasil = b < 3
print(b, '<',3, '=',hasil)
hasil = b < 2
print(b, '<',2, '=',hasil)

# lebih dari sama dengan >=
print("=============== lebih dari sama dengan (>=)")
hasil = a >= 3
print(a, '>=',3, '=', hasil)
hasil = b>= 3
print(b, '>=',3, '=', hasil)
hasil = b >= 2
print(b, '>=',2, '=', hasil)

# kurang dari sama dengan <=
print("=============== kurang dari sama dengan (<=)")
hasil = a <= 3
print(a, '<=',3, '=', hasil)
hasil = b <= 3
print(b, '<=',3, '=', hasil)
hasil = b <= 2
print(b, '<=',2, '=', hasil)

# sama dengan ==
print("=============== sama dengan (==)")
hasil = a == 4
print(a,'==',4, '=', hasil)
hasil = b ==4
print(b,'==',4, '=', hasil)

# tidak sama dengan !=
print("=============== tidak sama dengan (!=)")
hasil = a != 4
print(a,'!=',4, '=', hasil)
hasil = b != 4
print(b,'!=',4, '=', hasil)

# 'is' sebagai komparasi obj identity (bukan literal)
x = 5 # ini adalah assignment membuat object
y = 5
hasil = x is y
print('x is y:', hasil)

# ' is not' sebagai komparasi obj identity (nukan literal)
x = 5 # ini adalah asssignment membuat object
y = 6
hasil = x is not y
print('x is not y:', hasil)

# TUGAS PERTEMUAN 3
p = 12
l = 5
t = 8

hasil1 = 2*(p*l + p*t + l*t)
hasil2 = p*l*t
hasil3 = 4*(p+l+t)

print("Luas adalah", hasil1)
print("Volume adalah", hasil2)
print("Keliling adalah", hasil3)

hasil4 = 2* (p*l + p*t + l*t) > 50
hasil5 = p*l*t == 480
print("Apakah luas bangunan lebih luas dari 50?", hasil4)
print("Apakah volume sama dengan 480?", hasil5)