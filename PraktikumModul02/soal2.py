# 2. Sebuah mal menerapkan tarif parkir mobil sebagai berikut:
# - 2 jam pertama tarif flat: Rp 5.000 (total).
# - Setiap jam berikutnya dikenakan tambahan Rp 2.000 per jam.
# Buat program yang meminta input lama parkir (dalam jam), lalu hitung dan
# cetak total tarif parkir yang harus dibayar.
# Petunjuk: Lakukan pengecekan, jika jam <= 2, maka bayar 5000. Jika jam >
# 2, hitung selisih jamnya lalu kalikan 2000, kemudian tambah 5000. Buatlah
# pengimplementasian percabangan yang memiliki 3 kondisi dalam bahasa
# pemrograman python!

lama = float(input("Masukkan lama parkir: "))

if lama <= 0:
    print("Lama parkir tidak valid")

elif lama <= 2:
    bayar = 5000
    print(f"Total biaya parkir Rp{int(bayar)}")

else:
    selisih = lama - 2
    bayar = 5000 + (selisih * 2000)
    print(f"Total biaya parkir Rp{int(bayar)}")
