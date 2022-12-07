# 리스트에 들어있는 정수 중 짝수만 구하는 프로그램을 작성하세요. 만약 짝수가 없으면 0을 출력하세요.
a = int(input())
cnt = 0
for i in range(a) :
    b = int(input())
    if b % 2 == 0 :
        print(b, end=' ')
        cnt += 1

if cnt == 0 :
    print(cnt)