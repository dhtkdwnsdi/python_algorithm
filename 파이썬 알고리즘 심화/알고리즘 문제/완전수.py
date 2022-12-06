# 완전수란 자신을 제외한 모든 약수의 합이 자신과 같은 수를 말합니다.
#
# 입력값으로 범위를 입력하고 해당 범위 내의 완전수를 모두 출력하는 프로그램을 작성하세요.
a = input()
a = a.split()
b = []
hap = 0
for i in range(int(a[0]), int(a[1]) + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            if j != i:
                hap += j
    if hap == i:
        b.append(hap)
        hap = 0
    else:
        hap = 0

for i in b:
    print(i, end=' ')