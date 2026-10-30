# 2. Sebuah kantor layanan administrasi menggunakan struktur data List untuk menyimpan nomor antrean pelanggan. Pelanggan yang datang akan masuk ke bagian akhir antrean, sedangkan pelanggan yang berada di urutan paling depan akan dilayani terlebih dahulu.Untuk menjaga ketertiban antrean, sistem menyediakan empat operasi, yaitu MASUK, LAYANI, BATAL, dan TAMPIL. Buatlah program Python untuk mengelola antrean pelanggan menggunakan list dengan ketentuan sebagai berikut.

banyak = int(input("Masukkan jumlah operasi: "))

lst = []
lst_baru = []


for i in range(banyak):
  operasi = input(f"Operasi ke-{i + 1}: ")

  if operasi == "MASUK":
    nomer = int(input("Masukkan nomer pelanggan: "))
    lst += [nomer]

    print(f"Pelanggan {nomer} berhasil masuk")
    print(f"Antrean saat ini {lst}")
    print()

  elif operasi == "LAYANI":
    panjang = 0
    for i in lst:
      panjang += 1
    if panjang < 0:
      print("Tidak ada pelanggan yang akan dilayani")
      print(f"Antrean kosong")
    else:
      print(f"Pelanggan {lst[0]} berhasil dilayani")

      lst = lst[1:]

      print(f"Antrean Saat ini {lst}")
      print()

  elif operasi == "BATAL":
    nomer = int(input("Masukkan nomer antrean: "))

    if nomer in lst:
      for i in lst:
        if i != nomer:
          lst_baru += [i]
          lst = lst_baru[:]
        else:
          lst_baru += []
          lst = lst_baru[:]
      panjang = 0
      for i in lst:
        panjang += 1
      if panjang > 0:
        print(f"Antrean saat ini: {lst}")
        print()
      else:
        print("Antran kosong")
    else:
      print("Nomer antrean tidak terdaftar")

      print(f"Antrean saat ini: {lst}")
      print()

  elif operasi == "TAMPIL":
    panjang = 0
    for i in lst:
      panjang += 1

    if panjang > 0:
      print(f"Antrean saat ini: {lst}")
    else:
      print("Antrean kosong")

  else:
    print("Operasi Tidak Valid")