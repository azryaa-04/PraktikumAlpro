banyak = int(input("Masukkan jumlah data: "))

nilai = []
i = 1

while i <= banyak:
  data = int(input(f"Masukkan nilai ke-{i}: "))
  nilai += [data]
  i += 1
print(f"list yang terbentuk: {nilai}")