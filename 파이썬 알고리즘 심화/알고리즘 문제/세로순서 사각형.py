#
# 정사각형의 한 변의 길이 n을 입력받은 후 숫자로 된 정사각형 형태로 출력하는 프프로그램을 작성하세요.
#
# 숫자의 진행 순서는 처음에 왼쪽 위에서 아래쪽으로 n만큼 진행한 후 바로 오른쪽 위에서 다시 아래쪽으로 진행하여 정사각형이 될 때까지 반복하는 것입니다.
# 인풋 4
# 1 5 9 13
# 2 6 10 14
# 3 7 11 15
# 4 8 12 16
# 인풋 10
# 1 11 21 31 41 51 61 71 81 91
# 2 12 22 32 42 52 62 72 82 92
# 3 13 23 33 43 53 63 73 83 93
# 4 14 24 34 44 54 64 74 84 94
# 5 15 25 35 45 55 65 75 85 95
# 6 16 26 36 46 56 66 76 86 96
# 7 17 27 37 47 57 67 77 87 97
# 8 18 28 38 48 58 68 78 88 98
# 9 19 29 39 49 59 69 79 89 99
# 10 20 30 40 50 60 70 80 90 100
a = int(input())
for i in range(1, a+1) :
    for j in range(1, a+1) :
        print(i+(j-1)*a, end = ' ')
    print()