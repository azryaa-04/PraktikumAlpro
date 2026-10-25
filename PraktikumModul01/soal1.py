# 1. Buatlah program yang meminta pengguna memasukkan sebuah angka bulat yang mempresentasikan jumlah hari. Program harus menghitung dan mencetak berapa jumlah hari tersebut jika di ubah ke dalam jam, menit, detik.
# ➢ Rumus: 1 Hari = 24 jam, 1 jam = 60 menit, 1 menit = 60 detik
# ➢ catatan: jumlah hari menggunakan fungsi input()

day = int(input("Masukkan jumlah hari: "))

jam = day * 24
menit = jam * 60
detik = menit * 60

print(day, "hari ada",jam, "jam")
print(day, "hari ada",menit, "menit")
print(day, "hari ada",detik, "detik")
