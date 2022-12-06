#
# 아래의 조건을 만족하는 해를 윤년(Leap year)이라고 합니다.
#
# 연수가 4로 나누어 떨어지는 해는 윤년입니다.
# 이 중에서 100으로 나누어 떨어지는 해는 평년입니다.
# 그 중에서 400으로 나누어 떨어지는 해는 윤년입니다.
# 연도를 입력 받아 윤년인지 아닌지를 결정하는 프로그램을 작성하세요.
a = int(input())

if a % 4 == 0 :
    if a % 100 == 0 :
        if a % 400 == 0 : print('Leap Year')
        else : print('Not Leap Year')
    else : print('Leap Year')
else : print('Not Leap Year')    