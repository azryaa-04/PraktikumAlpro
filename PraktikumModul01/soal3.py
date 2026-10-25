# 3. Buatlah program menghitung diskon harga beli dari suatu barang Dimana terdapat tiga jenis inputan. Inputan pertama merupakan harga beli suatu barang, inputan kedua merupakan jumlah beli suatu barang, dan inputan ketiga merupakan diskon dari harga beli seluruh barang

harga = float(input("masukkan total harga: "))
jml = float(input("masukkan jumlah barang: "))
dis = float(input("masukkan diskon: "))

hasil = (harga * jml) - (harga * jml * dis / 100)

print("harga yang harus dibayar: ", int(hasil))
