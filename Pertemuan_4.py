# operasi logika atau boolean
# not, or, and, xor

print ('===NOT===')
a = True
b = not a
print ('data a =',a)
print ('------------ NOT')
print ('data b =',b)

# OR ( jika salah satu true, maka hasilnya adaalah true)
print ('===OR===')
a = False
b = False
c = a or b
print (a,'OR',b,'=',c)
a = False
b = True
c = a or b
print (a,'OR',b,'=',c)
a = True
b = False
c = a or b
print (a, 'OR',b,'=',c)
a = True 
b = True
c = a or b
print (a,'OR',b,'=',c)

# AND (jika dua buah nilai true, maka hasil true)
print ('===AND===')
a = False
b = False
c = a and b
print (a,'AND',b,'=',c)
a = False
b = True
c = a and b
print (a,'AND',b,'=',c)
a = True
b = False
c = a and b
print (a, 'AND',b,'=',c)
a = True 
b = True
c = a and b
print (a,'AND',b,'=',c)

# XOR (akan true jika salah satu true. sisanya false)
print ('===XOR===')
a = False
b = False
c = a ^ b
print (a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print (a,'XOR',b,'=',c)
a = True
b = False
c = a ^ b
print (a, 'XOR',b,'=',c)
a = True 
b = True
c = a ^ b
print (a,'XOR',b,'=',c)

# LATIHAN
inputUser = int(input("Masukkan usia : "))
if (inputUser <= 12):
    print("Anak-anak")
elif (inputUser > 12) and (inputUser <= 17):
    print("Remaja")
elif (inputUser > 17) and (inputUser <= 59):
    print("Dewasa")
else:
    print("Lansia")