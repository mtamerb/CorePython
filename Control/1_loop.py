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
