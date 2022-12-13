def checkH(a,b):
    global check
    if a == b : check = True
    else : check = False
check = False
a = input()
cnt = 1
for i in a :
    checkH(i, a[-cnt])
    cnt+=1

print(check)