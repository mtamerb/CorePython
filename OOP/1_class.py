# Kaynak : https://python-textbok.readthedocs.io/en/1.0/Classes.html#defining-and-using-a-class

# Python'da her şey bir nesnedir - her şey bir sınıfın örneğidir.

# Sınıf kullanımı

import datetime


class Kisi:
    """
     Python'da bir nesne çağırdığınızda otomatik olarak çalışacak ve sadece nesneyi ilk oluşturduğunuzda çalışacak olan
     bir fonksiyon tanımlayabilirsiniz.  __init__ , OOP ile programlamada bir class’ın initialiser( başlatıcı ) metodur.
     Class içinden türetilen nesnelere ait özellikler
     bu metot ile nesnelere atanır.
    """

    def __init__(self, isim, soy_isim, dogum_tarihi, adres, telefon, email):
        self.isim = isim
        self.soy_isim = soy_isim
        self.dogum_tarihi = dogum_tarihi
        self.adres = adres
        self.telefon = telefon
        self.email = email

    def yas(self):
        bugun = datetime.date.today()
        yas = bugun.year - self.dogum_tarihi.year
        if bugun < datetime.date(bugun.year, self.dogum_tarihi.month, self.dogum_tarihi.day):
            yas -= 1
        return yas


kisi = Kisi("Marlon", "Brando", datetime.date(1960, 4, 15), "DC 17th St.", "534 680 2321", "marlonbrando@example.com")

print("İsim : {} \nSoyİsim: {} \nDoğum Tarihi : {} \nYaş: {} \nAdres : {} \nTelefon: {} \nEmail: {} ".format(kisi.isim,
                                                                                                             kisi.soy_isim,
                                                                                                             kisi.dogum_tarihi,
                                                                                                             kisi.yas(),
                                                                                                             kisi.adres,
                                                                                                             kisi.telefon,
                                                                                                             kisi.email))

# instance : Python'da sınıfa ait nesnelerdir . örnek ->

i = kisi.isim = "Instance"
print(i)


