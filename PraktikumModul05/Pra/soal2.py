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
