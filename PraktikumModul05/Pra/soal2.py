# 2. Menghapus elemen List secara manual pada python program meminta pengguna memasukkan sebuah bilangan yang ingin dihapus dari List tersebut.
# Program harus menghapus seluruh kemunculan bilangan yang dipilih dengan cara membuat List baru yang hanya berisi elemen-elemen yang tidak sama dengan bilangan tersebut.
# Jika bilangan yang ingin dihapus tidak ditemukan, program harus menampilkan pesan bahwa data tidak ditemukan dan mempertahankan seluruh data awal.
# • Dilarang menggunakan metode .remove() untuk menghapus elemen List.
# • Penghapusan dilakukan dengan membuat List baru dan menyalin elemen yang tidak sama dengan nilai yang ingin dihapus.
# • Program harus menghapus seluruh kemunculan nilai yang dipilih, bukan hanya kemunculan pertama.

nilai = ["100","10","20","30","10","20","30","90","80","70","90","80","70","50","60","60","50","100",]

nilai_baru = []

print(f"list sebelum penghapusan: {nilai}")
hapus = (input("Masukkan bilangan yang ingin dihapus: "))
if hapus in nilai:
  for i in nilai:
    if i != hapus:
      nilai_baru += [i]
  print(f"list setelah penghapusan: {nilai_baru}")
else:
  print(f"elemen yang akan di hapus tidak terdapat didalam list")
  print(nilai)
