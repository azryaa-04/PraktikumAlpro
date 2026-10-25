# 1. Buatlah program yang meminta input Umur pengguna.
# - Jika umur >= 17, cetak "Anda sudah memenuhi syarat untuk membuat SIM."
# - Jika umur di bawah 17, hitung kekurangannya, lalu cetak "Anda belum cukup
# umur. Silakan tunggu [X] tahun lagi." (Ganti [X] dengan hasil perhitungan).

umur = int(input("Masukkan umur anda: "))

kurang = 17 - umur
if umur >= 17 :
  print("Anda sudah memenuhi syarat untuk membuat SIM")
else:
  print("Anda belum cukup umur. Silahkan tunggu",kurang, "tahun lagi.")
