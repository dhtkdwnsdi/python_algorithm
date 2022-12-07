# 입력된 문자열에서 공백을 제거하여 출력하세요.
#
# 예를 들어 "This is Sparta!"가 입력 되었다면 "ThisisSparta!"가 출력되도록 하면 됩니다.
a = input()
for i in a :
    if i == ' ' : i=''
    print(i, end='')