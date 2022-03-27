from math import factorial as fac

x = 4
y = 3
print(fac(x) / fac(y))
print(2 ** 31 - 1)
print(fac(13) > 2 ** 31 - 1)
n = 10
nK = fac(n)
nkLen = len(str(nK))
print(fac(n))
print(nkLen)
# 5 üssü 4
print(int("10000", 5))
#print(n is 10)
print(bool(19))
print(bool(0))

# while
"""
while True:
    response = input("input = ")
    print(response)
    if int(response) % 13 == 0:
        print("program is stopping")
        break
"""
try:
    while True:
        print(1)
except KeyboardInterrupt:
    print('interrupted!')
    exit()
