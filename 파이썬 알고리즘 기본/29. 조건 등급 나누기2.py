a = int(input())
score = ''
if a >= 81 and a <= 100 :
    score = 'A'
    print('{}점:{}등급'.format(a, score))
elif a>=61 and a < 80 :
    score = 'B'
    print('{}점:{}등급'.format(a, score))
elif a>=41 and a<60 :
    score = 'C'
    print('{}점:{}등급'.format(a, score))
else :
    print('등급없음')
