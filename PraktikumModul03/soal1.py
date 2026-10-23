angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

i = angka1
while i <= angka2:
  if i % 2 != 0:
    print(i)
  i += 1