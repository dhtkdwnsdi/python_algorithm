a = int(input())
score = ''
if a >= 81 :
    score = 'A'
elif a>=61 and a < 80 :
    score = 'B'
elif a>=41 and a<60 :
    score = 'C'
else :
    score = 'D'

print('{}점:{}등급'.format(a, score))