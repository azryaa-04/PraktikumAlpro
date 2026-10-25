# 3. Buatlah sebuah program Python untuk menyimpan sejumlah nilai ujian mahasiswa ke dalam sebuah Tuple. Program meminta pengguna memasukkan jumlah mahasiswa, kemudian memasukkan nilai ujian setiap mahasiswa satu per satu. Setelah seluruh nilai dimasukkan, program harus mengubah kumpulan nilai tersebut menjadi Tuple
#  Tuple yang berisi seluruh nilai mahasiswa.

MaafYaLagiSibukBaruSelesaiNgoding = int(input("Masukkan jumlah data: "))

LohKamuProgrammer = ()
AduhBlunderLagi = 1

while AduhBlunderLagi <= MaafYaLagiSibukBaruSelesaiNgoding:
  apaya = int(input(f"Masukkan nilai ke-{AduhBlunderLagi}: "))
  gatau = (apaya,)
  LohKamuProgrammer += gatau
  AduhBlunderLagi += 1

print(f"tuple yang terbentuk: {LohKamuProgrammer}")