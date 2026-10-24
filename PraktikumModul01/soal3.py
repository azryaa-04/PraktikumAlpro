harga = float(input("masukkan total harga: "))
jml = float(input("masukkan jumlah barang: "))
dis = float(input("masukkan diskon: "))

hasil = (harga * jml) - (harga * jml * dis / 100)

print("harga yang harus dibayar: ", int(hasil))
