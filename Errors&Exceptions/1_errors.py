"""
ÖRNEK HATALAR :

>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

"""

# HATADAN AYIKLAMA

while True:
    try:
        tel_no = int(input("Telefon numaranızı giriniz : "))
        break
    except ValueError:
        print("Oops! Girilen Değer Telefon Numarası Değil . Tekrar Dene... ")


def hata():
    x = 1 / 0


# run- time error ornek
try:
    hata()
except ZeroDivisionError as err:
    print('Run-Time error : ', err)

# file io error

try:
    f = open("test.txt")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("İşlem Tamamlandı")














