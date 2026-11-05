# # perulangan loop
# # angka = 1
# # print(angka)
# # angka = angka + 1
# # print(angka)
# # angka = angka + 1
# # print(angka)
# # for kondisi
# # aksi

# # dengan list
# angka2 = [0,1,2,3,4] # ini adalah list
# print(angka2)
# for i in angka2:
#     print(f"i sekarang -> {i}") 
# print("akhiri dari program\n")

# # dengan range
# angka3 = range(5)
# for i in angka3:
#     print(f"i sekarang -> {i}")
# print("akhiri dari program\n")

# angka4 = range(1,10)
# for i in angka4:
#     print(f"i sekarang -> {i}")
#     #print("saya keren")
# print("akhiri dari program\n")

# # menggunakan string
# data_str = "saya ganteng abiesssss"

# for huruf in data_str:
#     print(huruf)
# print("akhiri dari program\n")

# # while loop
# print ("===contoh 1===")
# angka = 1
# while angka > 5:
#     angka = angka +1
#     print("ipin lari ipin!!!")
# print ("===contoh 2===")
# angka = 0
# print(f"angka sekarang -> {angka}")
# while angka < 5:
#     angka += 1
#     #angka = angka + 1
#     print(f"angka sekarang -> {angka}")
#     print("ipin lari ipin")
# print ("program berakhir, ipin sudah jauh")

# # continue and pass
# # pass -> dia berfungsi sebgai dummy, tidak akan dieksekusi

# # passs
# angka = 0
# while angka < 5:
#     angka = angka + 1

#     if(angka == 3):
#         pass;
#     print(angka)

# # continue
# angka = 0
# print(f"angka sekarang -> {angka}") # aksi 1
# if(angka ==3):
#     print("nice")
# print("whassup") # aksi 2
# print("finish")

# # break
# angka = 0
# print(f"angka sekarang -> {angka}")
# while angka < 5:
#     angka = angka + 1
#     print(f"angka sekarang")
# # if(angka == 3)
#     print("nice")
#     break
# print("whassup")
# print("cukup mas")

# # 5.5 pengulangan
# # membuat segitiga
# # for
# sisi = 4
# count = 1

# for i in range(sisi) : 
#     print("*" * count)
#     count += 1

# # while
# sisi = 4
# count = 1

# while True:
#     print("*" * count)
#     count += 1

#LATIHAN
#Membuat program yang menampilkan bilangan ganjil dan genap dengan menggunakan perulangan
print ("BILANGAN GENAP DAN GANJIL")
bilangan = range(1,51)
for x in bilangan:
    if (x % 2 == 0):
        print(f" {x} bilangan genap")
    else:
        print(f"{x} bilangan ganjil")
print ("SELESAI")
# membuat program yang menampilkan bilangan prima antara 1 sampai 100 dengaan menggunakan perulangan
print ("BILANGAN PRIMA")
for bilangan in range(1, 101):
    if bilangan > 1:
        for x in range(2, bilangan):
            if (bilangan % x) == 0:
                break
        else:
            print(bilangan, "termasuk bilangan prima")
print ("SELESAI")