# 3. Pemisahan Data Berdasarkan Kriteria
# Diberikan data kelulusan tes fisik:
# data_peserta = {"Peserta_1": 165, "Peserta_2": 150, "Peserta_3": 170, "Peserta_4": 155}
# (Nilai tersebut adalah tinggi badan dalam cm).
# Buatlah dua Dictionary kosong: lulus = {} dan gagal = {}.
# Gunakan perulangan pada data_peserta. Jika tinggi badan >= 160, pindahkan data tersebut ke Dictionary lulus. Jika di bawah 160, pindahkan ke gagal. Cetak kedua Dictionary tersebut secara terpisah.

peserta = {
    "aku": 195,
    "kamu": 185,
    "dia": 143,
    "dilan": 155
}
lulus = {}
gagal = {}

for i in peserta:
  if peserta[i] >= 160:
    lulus[i] = peserta[i]
  else:
    gagal[i] = peserta[i]
print("data peserta")
for i in peserta:
  print(f"{i} | {peserta[i]}")
print()
print("yang lulus")
print(lulus)
print("yang gagal")
print(gagal)
    
