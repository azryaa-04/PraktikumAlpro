# 1. Buatlah algoritma dengan menggunakan flowchart dan implementasikan dengan bahasa pemrograman Python untuk menampilkan suku-suku yang terdapat pada deret aritmatika dan jumlah total suku-suku tersebut, dengan ketentuan sebagai berikut :
# a. suku awal dan beda dari deret aritmatika yang akan dibentuk, merupakan inputan dari pengguna
# b. suku terakhir dari deret aritmatika, tidak boleh melebihi dari nilai yang telah ditentukan dari pengguna, seperti yang dicontohkan pada Gambar 1

a = int(input("Masukkan Suku awal: "))
b = int(input("Masukkan beda: "))
n = int(input("Masukkan Suku terakhir: "))

jumlah = 0

for i in range(a, n, b):
    print("suku # 1: ", i)
    jumlah += i
print("Total deret:",jumlah)
