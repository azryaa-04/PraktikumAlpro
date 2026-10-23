a = int(input("Masukkan Suku awal: "))
b = int(input("Masukkan beda: "))
n = int(input("Masukkan Suku terakhir: "))

jumlah = 0

for i in range(a, n, b):
    print("suku # 1: ", i)
    jumlah += i
print("Total deret:",jumlah)
