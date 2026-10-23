total = 0
banyak = 0

while True:
  nilai = float(input("Masukkan Nilai: "))
  if nilai != 0:
    total += nilai
    banyak += 1
  else:
    break

print("Total: ",int(total))
print("angka yang dimasuk kan: ",banyak)
print("Rata rata: ",total/banyak)