# 4. Di Python, operator perkalian * bisa digunakan pada teks. Contoh: "" * 3 akan menghasilkan "**".
# Buat program yang meminta input Tinggi Segitiga (angka bulat). Gunakan while untuk mencetak pola bintang dari 1 baris hingga setinggi angka tersebut.

tinggi = int(input("Masukkan tinggi: "))

i = 1
while i <= tinggi :
  print(i * "*")
  i += 1
