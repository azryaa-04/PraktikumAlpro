# 1. Aplikasi Kamus Penerjemah Mandiri
# Buatlah Dictionary yang berisi 5 pasang kata (contoh: "makan": "eat", "tidur": "sleep").
# Program meminta input sebuah kata dalam bahasa Indonesia. Gunakan perulangan untuk mencari terjemahannya.
# Jika kata tersebut tidak ditemukan di dalam kamus Anda, program harus meminta input terjemahannya dari pengguna, lalu menambahkan pasangan kata baru tersebut ke dalam Dictionary Anda agar kamusnya semakin pintar. Tampilkan isi kamus terbaru!

kata = {"tidur":"sleep"}
while True:
  masukan = input("Masukkan sebuah kata: ")
  if masukan in kata:
    for i in kata:
      if i == masukan:
        print(f"bahasa inggris nya {masukan} adalah {kata[i]}")

  else:
    print("kata belum ada di kamus")
    translate = input("masukkan arti katanya: ")
    kata[masukan] = translate
    for i in kata:
      print(f"{i} : {kata[i]}")