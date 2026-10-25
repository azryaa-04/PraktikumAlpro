# 3. Buat Code untuk mengkonversikan bilangan biner menjadi bilangan desimal

biner = input("Masukkan angka biner: ")

biner = biner[::-1]
total = 0

p = 0
for i in biner:
    desimal = int(i) * 2 ** p
    total += desimal
    p += 1

print(f"angka desimal dari angka biner tersebut ialah: {float(total)}")