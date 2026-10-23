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

