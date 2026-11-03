# 4. Mencari Nilai Maksimal dalam Dictionary Diberikan data penjualan barang: penjualan = {"Sepatu": 45, "Tas": 60, "Topi": 25, "Kemeja": 80, "Celana": 50}
# Tanpa menggunakan fungsi max(), gunakan perulangan untuk mencari tahu nama barang apa yang paling banyak terjual dan berapa jumlahnya.
# Petunjuk: Buat variabel angka_terbesar = 0 dan barang_terlaris = "".
# Setiap kali perulangan menemukan nilai yang lebih besar dari angka_terbesar, perbarui kedua variabel tersebut.

penjualan = {"Sepatu": 45, "Tas": 60, "Topi": 25, "Kemeja": 80, "Celana": 50}

terlaris = 0
barang = ""
for i in penjualan:
  if penjualan[i] > terlaris:
    terlaris = penjualan[i]
    barang = i
print(terlaris)
print(barang)
