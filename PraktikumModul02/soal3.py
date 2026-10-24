namaPembeli = input("Masukkan nama anda: ")
totalBelanja = float(input("total belanjaan: "))
statusMember = input("status member(iya/tidak): ")
jumlahBarang = int(input("jumlah barang: "))

gratisOngkir = "Tidak mendapatkan gratis ongkir"
if totalBelanja >= 500000 :
  if statusMember == "iya" :
    diskon = 20
    totalSetelahDiskon = totalBelanja - (totalBelanja * (diskon / 100))
    if totalSetelahDiskon >= 500000:
      gratisOngkir = "Mendapatkan gratis ongkir"
    else:
      gratisOngkir = "Tidak mendapatkan gratis ongkir"
  else:
    diskon = 10
    totalSetelahDiskon = totalBelanja - (totalBelanja * (diskon / 100))
    gratisOngkir = "Tidak mendapatkan gratis ongkir"
else:
  if jumlahBarang >= 5 :
    diskon = 5
    totalSetelahDiskon = totalBelanja - (totalBelanja * (diskon / 100))
  else:
    diskon = 0
    totalSetelahDiskon = totalBelanja
print()
print("======STRUK BELANJA=====")
print("Nama pembeli: ",namaPembeli)
print("total belanja: ",int(totalBelanja))
print("Status member: ",statusMember)
print("Jumlah barang: ",jumlahBarang)
print(f"diskon: {diskon}%")
print(f"harga akhir yang harus dibayar: {int(totalSetelahDiskon)}")
print(gratisOngkir)
