# 1. Menambahkan elemen pada list seacara manual Buatlah sebuah program Python untuk menampung sejumlah bilangan bulat ke dalam sebuah List. Program meminta pengguna memasukkan jumlah data yang ingin disimpan, kemudian meminta pengguna memasukkan setiap bilangan satu per satu.
# Setiap bilangan yang dimasukkan harus ditambahkan ke dalam List menggunakan operator penjumlahan (+) dengan membungkus bilangan baru di dalam kurung siku.
#  List harus diinisialisasi sebagai List kosong.
#  Penambahan data wajib menggunakan operator + dengan format data = data + [nilai_baru].
#  Dilarang menggunakan metode .append() untuk menambahkan elemen.
#  Program harus menggunakan perulangan untuk menerima masukan data.
#  Program harus menampilkan List akhir dan jumlah elemen yang berhasil dimasukkan.

banyak = int(input("Masukkan jumlah data: "))

nilai = []
i = 1

while i <= banyak:
  data = int(input(f"Masukkan nilai ke-{i}: "))
  nilai += [data]
  i += 1
print(f"list yang terbentuk: {nilai}")