# 1. Buat program yang meminta dua angka dari pengguna: Angka Awal dan Angka Akhir. Gunakan perulangan while untuk mencetak semua bilangan ganjil yang berada diantara Angka Awal hingga Angka Akhir tersebut.
# Petunjuk: Gabungkan while dengan if dan operasi Modulo % di dalamnya.

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

i = angka1
while i <= angka2:
  if i % 2 != 0:
    print(i)
  i += 1