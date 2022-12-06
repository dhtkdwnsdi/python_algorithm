# 3의 배수 게임이란? 여러 사람이 순서를 정해 순서대로 수를 부르는 게임이다.
# 만약 3의 배수를 불러야 하는 상황이라면, 그 수 대신 “박수”를 친다.
a = int(input())

for i in range(1, a+1):
    if i % 3 ==0 : print('X', end=' ')
    else : print(i, end=' ')