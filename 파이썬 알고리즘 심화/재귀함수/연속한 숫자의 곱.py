def multiNum(a):
    global b
    b = b*a

a = int(input())
b = 1
for i in range(1, a+1) :
    multiNum(i)
print(b)