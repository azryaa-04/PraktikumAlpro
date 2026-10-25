# 2. Buatlah program yang meminta pengguna untuk memasukkan Nilai tugas, UTS, dan UAS.
# ✓ Nilai tugas: 20%
# ✓ Nilai UTS: 40%
# ✓ Nilai UAS: 40%
# Rumus: (tugas * 20%) + (UTS * 40%) + (UAS * 40%)

tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

hasil = (tugas * 20 / 100) + (uts * 40 / 100) + (uas * 40 / 100)
print("Nilai rata rata: ",hasil)
