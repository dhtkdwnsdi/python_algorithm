a = []
while True:
    b= int(input())
    if b == 0 :
        break
    a.append(b)

print('{} 평균:{}'.format(a, sum(a)/len(a)))