# anahtar - değer eşlemeli (ilişkisel ) dizi
telefon_no = {"Turgut": "534-678-9023",
              "Buse": "543-123-4567",
              "Nur": "532-678-5643",
              "Sezer": "555-320-4568"}
print("Nur\'un Telefon Numarası    : " + telefon_no["Nur"])
print("Turgut\'un Telefon Numarası : " + telefon_no["Turgut"])
print("Sezer\'in Telefon Numarası  : " + telefon_no["Sezer"])

# dict veri türünün bazı methodları
print("\nTelefon Numaralarının Listelenmiş Hali : " + str(list(telefon_no.values())))
print("Telefon Numaralarının Sıralanmış  Hali : " + str(sorted(telefon_no.values())))

#  Sözlükler arasında dolaşırken, item() yöntemi kullanılarak anahtar ve karşılık gelen değer aynı anda alınabilir.
print()
film_oyuncu_karakter = {"Keanu Reeves": "=> Neo",
                        "Carrie-Anne Moss": "=> Trinity",
                        "Laurence Fishburne": "=> Morpheus",
                        "Hugo Weaving": "=> Ajan Smith"}
for k, v in film_oyuncu_karakter.items():
    print(k, v)

# numaralandırılmış
print()
for k, v in enumerate(["Moby Dick", "Vakıf", "Dune", "Üç Silahşörler"]):
    print(k, v)

# for - loop
print()
araba_markaları = ["Audi", "Bmw", "Mercedes-Benz", "Bentley", "Porsche", "Honda"]
for araba in araba_markaları:
    print(araba)

# for -loop , key- value  kullanımı
print()
for actors in film_oyuncu_karakter:
    print(actors, film_oyuncu_karakter[actors])
