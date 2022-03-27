def square(x):
    return x * x


print("Karesi : " + str(square(13)))



def iki_sayinin_toplami(x, y):
    return x + y


print("Toplam : " + str(iki_sayinin_toplami(146, 54)))


def fonksiyonu_tanimlama():
    print("Başarılı Bir Şekilde Fonksiyon Tanımlandı .")


fonksiyonu_tanimlama()

inpt = int(input())


def tek_veya_cift(inpt):
    if inpt % 2 == 0:
        print(str(inpt) + " => Çift")
        return
    print(str(inpt) + " => Tek")


tek_veya_cift(inpt)
