# multiline strings
metin = """multiline 
satır 
örnek """
print(metin)
# ya da escape karakter
escape = " \nBu bir escape\nkarakter kullanılmış\nmetindir"
print(escape)
#  başka örnek kullanımlar
tirnak_metin = "Bu Tamer\'in Yazmış Olduğu Python Kodudur."
print(tirnak_metin)
# path için r , bu bizi 2 slash dan ( çirkin bir görüntü ) kurtarır.
path = r'C:\Users\tamer\OneDrive\Resimler'
print(path)

s = "şövalye"
print(s[1])
print(type(s[3]))
print(s.capitalize())
