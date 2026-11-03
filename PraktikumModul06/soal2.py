# 2. Rekapitulasi Suara (Voting System)
# Diberikan sebuah List statis yang berisi hasil pungutan suara pemilihan ketua kelas (terdapat data ganda):
# suara = ["Adi", "Izal", "Budi", "Siti", "Adi", "Izal", "Izal", "Budi"]
# Hanya berbekal List tersebut, buatlah Dictionary kosong bernama rekap_suara = {}.
# # Gunakan perulangan untuk membaca isi List, lalu gunakan Dictionary untuk menghitung total suara yang didapatkan oleh masing-masing kandidat secara otomatis. Cetak hasil akhirnya!

lst = ["aku", "kamu", "dia", "ubay", "raka", "Akbar", "aku", "kamu", "dia"]

rekap = {}
for i in lst:
  if i in rekap:
    rekap[i] += 1
  else:
    rekap[i] = 1

for k in rekap:
  print(f"{k} | {rekap[k]}")