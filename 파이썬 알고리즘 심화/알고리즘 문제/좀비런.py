# 구름이는 좀비런 대회에 참가했습니다. 좀비로 분장한 스태프들이 참가자들을 쫓아다니는 대회입니다.
#
# 너무 빨리 달려버리면 긴장감이 없어서 따분할 것 같은 구름이는 좀비들의 속도를 알기 때문에 잡히지 않는 최소한의 속도로 달리려고 합니다.
#
# 구름이가 먼저 출발하고 좀비들이 쫓아올 때 구름이가 잡히지 않을 최소 속도를 출력하는 프로그램을 작성해보세요.
a = input()
a = a.split()
b = 0
for i in a :
    if int(i)>b : b=int(i)
print(b)