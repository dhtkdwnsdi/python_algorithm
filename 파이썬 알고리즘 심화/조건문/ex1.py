a = input()
a = a.split()
b = 0
for i in a :
    b += int(i)
score = ''
if (b/3) >= 90 :
    score = 'A'
elif (b/3) >= 80 and (b/3) < 90:
    score = 'B'
elif (b/3) >= 70 and (b/3) < 80:
    score = 'C'
elif (b / 3) >= 60 and (b / 3) < 70:
    score = 'D'
else:
    score ='F'

print('{:.2f} {}'.format((b/3), score))