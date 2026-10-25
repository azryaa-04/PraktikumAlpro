# 2. Buat sebuah game sederhana. Tetapkan sebuah angka rahasia di dalam kode Anda
# (misalnya: angka_rahasia = 8).
# Beri kesempatan pengguna untuk menebak maksimal 3 kali.
# Jika tebakan benar, cetak "Selamat, tebakan Anda benar!" lalu program berhenti
# (break).
# Jika salah, beri tahu "Tebakan salah, sisa percobaan: [sisa]"
# Jika sudah 3 kali salah, cetak "Game Over. Anda kalah."

i = 2
while i >= 0:
  angka = int(input("Masukkan angka: "))
  if angka == 8 :
    print("Selamat, tebakan Anda benar!")
    break
  elif angka !=8 and i > 0:
    print(f"Tebakan salah, sisa percobaan:{i}")
  else:
    print("Game Over. Anda kalah")
  i -= 1

