# 3. Sebuah toko memberikan diskon berdasarkan total belanja dan status member.
# Program menerima:
# - Nama pembeli
# - Total belanja
# - Status member (ya/tidak)
# - Jumlah barang
# Ketentuannya:
# 1. Jika total belanja >= Rp500.000, cek status member.
# - Jika member:
# Hitung diskon 20% dari total belanja.
# Hitung total setelah diskon.
# Jika total setelah diskon >= Rp500.000, dapat gratis ongkir.
# Jika kurang dari Rp500.000, tidak mendapat gratis ongkir.
# - Jika bukan member:
# Hitung diskon 10%.
# Hitung total setelah diskon.
# Tidak mendapat gratis ongkir.
# 2. Jika total belanja < Rp500.000:
# Cek jumlah barang.
# Jika jumlah barang >= 5, dapat diskon 5%.
# Hitung total setelah diskon.
# Jika kurang dari 5 barang, tidak mendapat diskon.

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
