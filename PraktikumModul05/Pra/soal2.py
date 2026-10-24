MaafYaLagiSibukBaruSelesaiNgoding = int(input("Masukkan jumlah data: "))

LohKamuProgrammer = ()
AduhBlunderLagi = 1

while AduhBlunderLagi <= MaafYaLagiSibukBaruSelesaiNgoding:
  apaya = int(input(f"Masukkan nilai ke-{AduhBlunderLagi}: "))
  gatau = (apaya,)
  LohKamuProgrammer += gatau
  AduhBlunderLagi += 1

print(f"tuple yang terbentuk: {LohKamuProgrammer}")