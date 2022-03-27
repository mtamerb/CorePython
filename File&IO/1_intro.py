# Biçimlendirilmiş Dize Değişmezleri - f string
print("\n-------- f string -------------\n")
isim = "Tamer"
yas = 22

print(f"isim : {isim} yaş : {yas}")

evet_oyu = 42_572_654
hayır_oyu = 43_132_495
oran = evet_oyu / (evet_oyu + hayır_oyu)
print('\n{} Evet oyu: {:2.2%}'.format(evet_oyu, oran))

grup_yasi = {"Tamer": 22, "Duygu": 29, "Ceyda": 17}
for isim, yas in grup_yasi.items():
    print(f"\n{isim:10}=>{yas:10d}")

# String format() Yöntemi - str.format
print("\n-------- str.format -------------")
print("\n{} ve {} karada yaşar".format("Kurtlar", "Köpekler"))

print("sayı    karesi    küpü")
for x in range(1, 11):
    print('{0:2d} {1:9d} {2:9d}'.format(x, x * x, x * x * x))

# Dosyaları Okuma ve Yazma
# open() dosya nesnesi döndür.

# Okuma -
with open("dosya.txt", "r+") as f:
    # icerik = f.read()
    # print(icerik)
    for line in f:
        print(line, end="")

# Yazma -

for i in range(4):
    with open("dosya.txt", "a") as f:
        f.write("\n YAZMA GERCEKLESTİ ")
with open("dosya.txt", "r+") as f:
    # icerik = f.read()
    # print(icerik)
    for line in f:
        print(line, end="")