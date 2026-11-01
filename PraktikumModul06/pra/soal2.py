# 3. Menghitung Frekuensi Huruf
# Buatlah program yang meminta input sebuah kata atau kalimat. Program harus menghitung berapa kali masing-masing huruf muncul di dalam kalimat tersebut dan menyimpannya ke dalam sebuah Dictionary kosong frekuensi = {}.
# Petunjuk: Lakukan perulangan pada kalimat. Cek apakah huruf tersebut sudah ada sebagai kunci di dalam frekuensi. Jika belum ada, buat kuncinya dan beri nilai 1. Jika sudah ada, tambahkan nilainya dengan 1.

kata = input("Masukkan sebuah kata: ")
data = {}
for i in kata:
  data[i] = 0
  for k in kata:
    if i == k:
      data[i] += 1
print(data)
for d in data:
  print(f"huruf '{d}' muncul sebanyak {data[d]}")