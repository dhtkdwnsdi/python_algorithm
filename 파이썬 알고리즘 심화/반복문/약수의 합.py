# 자연수 n이 주어졌을 때 n의 약수의 합을 구하는 프로그램을 작성하세요.
#
# 예를 들어 n이 20이라면 20의 약수는 1, 2, 4, 5, 10, 20 이므로 답은 42가 됩니다.
a = int(input())
sumNum = 0

for i in range(1, a+1):
    if a % i ==0 : sumNum+=i

print(sumNum)