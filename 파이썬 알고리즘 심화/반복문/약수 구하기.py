#
# 양의 정수를 입력 받고 그 수의 약수를 모두 출력하는 프로그램을 작성하세요.
a = int(input())

for i in range(1, a+1):
    if a % i == 0 : print(i, end =' ')