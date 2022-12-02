a = []
while True:
    b= int(input())
    if b == 0 :
        break
    elif b>0 :
        a.append(b)

print('{} 평균:{}'.format(a, sum(a)/len(a)))