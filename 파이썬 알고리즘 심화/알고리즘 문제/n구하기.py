# 1 + 2 + 3 + 4 + .... + n 인 수가 입력받은 수를 넘어서는 시점에서의 n을 구하는 프로그램을 만드세요.
a = int(input())
sum_num = 0
cnt = 1

while True :
    sum_num += cnt
    if sum_num >= a : break
    cnt += 1
print(cnt)