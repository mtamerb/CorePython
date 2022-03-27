x = 500
x = 1000
y = x
x = 900
print(x)
print(y)

print(x is y)
print(id(x))
print(id(y))

# nesne atıf kontrolü
list = [12, 34, 56]

b_list = list


def call():
    print("\n" + str(list))
    print(b_list)


call()
b_list[1] = 100;
call()

# b_list listesinin 1.öğesindeki değişiklik list listesinde de değişikliğe uğradı . Aynı nesneye atıf'dan kaynaklı .
