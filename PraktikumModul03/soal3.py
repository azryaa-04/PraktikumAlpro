# 3. Buat program yang terus-menerus meminta pengguna memasukkan angka (nilai ujian) ke dalam sebuah mesin.
# Gunakan pola while True dan sebuah variabel total. selain menghitung total nilai, program juga harus menghitung berapa banyak angka yang dimasukkan (gunakan variabel penghitung tambahan/counter).
# Jika pengguna memasukkan angka 0, program harus melakukan break. Setelah break, program mencetak rata rata dari semua angka yang dimasukkan.

total = 0
banyak = 0

while True:
  nilai = float(input("Masukkan Nilai: "))
  if nilai != 0:
    total += nilai
    banyak += 1
  else:
    break

print("Total: ",int(total))
print("angka yang dimasuk kan: ",banyak)
print("Rata rata: ",total/banyak)