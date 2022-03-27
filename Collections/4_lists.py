l = [1, 4, 6]
print(l)
l[0] = "Şeftali"
print(l)

l2 = []
# liste sonuna ekleme için append methodu kullanırız.
l2.append("B")
l2.append("Liste")
l2.append("A")
print(l2)
l2.reverse()
objeCount = l2.count("obje")
print("obje kelimesi " + str(objeCount) + " defa görünür")
l2.insert(2, "obje")
l2.insert(3, "obje")
l2.insert(4, "obje")
objeCount = l2.count("obje")
print("Obje kelimesi Eklendi")
print("obje kelimesi " + str(objeCount) + " defa görünür")
print(l2)
print(list("karakterler"))
l2.sort()
print(l2)
print("---------------------------------------------------------")
# ---------------------------------------------------------------
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))

print(fruits.count('tangerine'))


fruits.index('banana')

fruits.index('banana', 4)  # Find next banana starting a position 4

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

fruits.pop()
print("---------------------------------------------------------")
# ---------------------------------------------------------------
