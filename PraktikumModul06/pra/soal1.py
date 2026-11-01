# 2. Pencarian Nilai Manual (Linear Lookup).
# Diberikan Dictionary berisi data nilai: nilai_siswa = {"Andi": 80, "Budi": 90, "Cici": 75, "Dedi": 60}
# Buatlah program yang meminta input sebuah nama dari pengguna. Gunakan perulangan for untuk mencari apakah nama tersebut ada sebagai kunci di dalam Dictionary.
# - Jika ditemukan, cetak "Nilai [Nama] adalah [Nilai]".
# - Jika sampai akhir perulangan tidak ditemukan, cetak "Data siswa tidak ditemukan".

nilai_mhs = {"Andi": 80, "Budi": 90, "Cici": 75, "Dedi": 60}

nama = input("Masukkan nama mahasiswa: ")
if nama in nilai_mhs:
  for i in nilai_mhs:
    if i == nama:
      print(f"Nilai {nama} adalah {nilai_mhs[i]}")
else:
  print("Nama mahasiswa tidak terdaftar")