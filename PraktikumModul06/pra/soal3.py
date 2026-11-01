# 4. Menggabungkan Dua Dictionary
# Diberikan dua buah Dictionary:
# kategori_A = {"Buku": 5, "Pensil": 10}
# kategori_B = {"Penghapus": 3, "Penggaris": 2}
# Buatlah sebuah Dictionary baru bernama gabungan = {}. Gunakan dua perulangan for secara berurutan untuk memindahkan seluruh isi kategori_A dan kategori_B ke dalam gabungan. Cetak Dictionary gabungan di akhir program.

a = {"Buku": 5, "Pensil": 10}
b = {"Penghapus": 3, "Penggaris": 2}

gabungan = {}

for i in a:
  gabungan[i] = a[i]

for k in b:
  gabungan[k] = b[k]

for i in gabungan:
  print(f"{i}: {gabungan[i]}")