a = int(input())
sumA = 0
sumB = 0
for i in range(a+1):
    if i%2 == 1 :
        sumA += i
    else:
        sumB+=i

print('1에서 {}까지 홀수의 합은 {}입니다.'.format(a, sumA))
print('1에서 {}까지 짝수의 합은 {}입니다.'.format(a, sumB))