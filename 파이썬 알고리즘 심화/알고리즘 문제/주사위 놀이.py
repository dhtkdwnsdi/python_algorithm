# 두개의 주사위를 가지고 입력 받은 숫자가 나올 경우를 모두 출력하세요.
# 예를 들을 5를 입력하면 1 4, 2 3, 3 2, 4 1 이 한 줄씩 출력되면 됩니다.
# *주사위는 육면체입니다.
a = int(input())
for i in range(1,7) :
    for j in range(1,7) :
        if i + j == a :
            print('{} {}'.format(i, j))