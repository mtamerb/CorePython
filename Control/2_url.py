from urllib.request import urlopen

story = urlopen("http://sixty-north.com/c/t.txt")
# kelimeleri tutmak için
story_kelimeler = []
for satir in story:
    satir_kelime = satir.split()
    for word in satir_kelime:
        story_kelimeler.append(word)

story.close()
print(story_kelimeler)

# output daki b' ifadesi bayt anlamındadır
if b'A' == b'\x41':
    print(True)
    if 'A' != b'A':
        print(True)
print("------------------------------------------------")
# b' notasyonunu decode ile kaldırdık
story = urlopen("http://sixty-north.com/c/t.txt")
# kelimeleri tutmak için
story_kelimeler = []
for satir in story:
    satir_kelime = satir.decode("utf8").split()
    for word in satir_kelime:
        story_kelimeler.append(word)

story.close()
print(story_kelimeler)

# decode encode utf8

s = "Hello World"
encoded = s.encode("UTF-8")
decoded = encoded.decode("UTF-8")
print("\nEncoded String:", encoded)
print("Decoded String  :", decoded)