angka = float(input("Masukkan bilangan desimal: "))

bulat = int(angka)
desimal = round(angka - bulat, 2)
biner = "."
cukup = 0

while True:
  if bulat % 2 == 0:
    biner = "0" + biner
  else:
    biner = "1" + biner

  bulat = bulat // 2 

  if bulat == 0 :
    break

i = 0
while i < 4  and desimal != 0.0:
  desimal = desimal * 2

  if desimal >= 1:
    biner += "1"
    bulat2 = round(desimal - 1, 2)
    desimal = bulat2
  else:
    biner += "0"

  i += 1

print(biner)