a = int(input())
b = []
while True :
    c = a%2
    a = int(a/2)
    b.append(c)
    if a < 2:
        b.append(a)
        break
b.reverse()

for i in b: print(i, end='')