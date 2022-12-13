def sumnum(b):
    global sumNum
    global a
    b = a % 10
    a = int(a/10)
    sumNum += b

sumNum = 0
a = int(input())
for i in range(len(str(a))):
    sumnum(a)
print(sumNum)