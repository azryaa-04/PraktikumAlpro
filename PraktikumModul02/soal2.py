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
