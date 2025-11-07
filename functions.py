# No argument taken, no return given
def greet():
    print("Halo, selamat datang")
 
greet()
 
# No argumen taken, return something
def get_pi():
    return 3.14
 
# hasil = get_pi()
# print(hasil)
 
 
#Menghitung luas lingkaran dengan pi yang sudah ada
def luas_lingkaran(jari_jari):
    pi = get_pi()
    return pi * jari_jari * jari_jari
 
r = float(input("Masukkan jari-jari lingkaran :" ))
luas = luas_lingkaran(r)
print(f"Luas lingkaran: {luas}")
 
 
# Takes arguments, no return given
def greet_nama(nama):
    print(f"Halo, {nama}")
 
greet_nama("Amin")
 
# Takes arguments, return something
# Fungsi penjumlahan
def summ (a,b):
    return a + b
 
hasil = summ (10,5)
print(hasil)
 
#Fungsi pengurangan
def summ (a,b):
    return a - b
 
hasil = summ (10,5)
print(hasil)
 
#Fungsi perkalian
def summ (a,b):
    return a * b
 
hasil = summ (10,5)
print(hasil)
 
#Fungsi pengurangan
def summ (a,b):
    return a / b
 
hasil = summ (10,5)
print(hasil)
