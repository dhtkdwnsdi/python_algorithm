fruits={'사과':2000, '배':3000, '감':1500}
a = input()
b = int(input())
fruits[a] = b
for i in fruits :
    print('{} : {}'.format(i, fruits[i]))