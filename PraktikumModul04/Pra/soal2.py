# 2. Buat kode bahasa pemrograman python menentukan kata palindrome check secara manual tanpa menggunakan METHOD apa pun!! :
# (a) katak = True (b) kasur = False (c) kasur rusak = True

kata ="katak"
balik =""
for huruf in kata:
  balik = huruf + balik
print(kata, "=", kata == balik)

kata ="kasur"
balik =""
for huruf in kata:
  balik = huruf + balik
print(kata, "=", kata == balik)

kata ="kasur rusak"
katanew =""
balik =""
for huruf in kata:
  if huruf != " ":
    katanew += huruf
    balik = huruf + balik
print(kata, "=", katanew == balik)