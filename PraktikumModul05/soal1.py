# # 1. Sebuah robot bergerak pada bidang dua dimesi (x, y). untuk mengetahui posisi robot, sistem harus menyimpan beberapa titik yang dimasukkan oleh pengguna Setiap titik koordinat di presentasikan dalam menggunakan tuple (x, y) sedangkan seluruh titik koordinat disimpan dalam list.
# Anda diminta membuat program untuk mencatat posisi robot dan menentukan titik koordinat yang paling jauh dari titik pusat (0, 0).
#Sebuah robot bergerak pada bidang dua dimesi (x, y). untuk mengetahui posisi robot, sistem harus menyimpan beberapa titik yang dimasukkan oleh pengguna
# Setiap titik koordinat di presentasikan dalam menggunakan tuple (x, y) sedangkan seluruh titik koordinat disimpan dalam list.
# Anda diminta membuat program untuk mencatat posisi robot dan menentukan titik koordinat yang paling jauh dari titik pusat (0, 0).

banyak = int(input("Masukkan banyak data:  "))

lst = []
tp = ()
for i in range(banyak):
  x = int(input(f"Masukkan koordinat ke-{i + 1} X: "))
  y = int(input(f"Masukkan koordinat ke-{i + 1} Y: "))
  koordinat = (x,y)
  lst = lst + [koordinat]
  i += 1

for i in lst:
  jarak = i[0] ** 2 + i[1] ** 2

  palingJauh = 0

  if palingJauh < jarak:
    palingJauh = jarak
    tp = (i[0],i[1])


print(lst)
print(tp)
print(f"Jarak paling jauh dari titik pusat: {palingJauh}")