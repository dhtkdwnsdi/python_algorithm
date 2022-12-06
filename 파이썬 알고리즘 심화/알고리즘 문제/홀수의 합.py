#
# 수의 범위가 입력되면 해당 범위 내의 홀수들의 합을 구하는 프로그램을 작성하세요.
a = int(input())
b = int(input())
sumNum = 0
for i in range(a, b+1) :
    if i % 2 ==1 : sumNum += i
print(sumNum)
