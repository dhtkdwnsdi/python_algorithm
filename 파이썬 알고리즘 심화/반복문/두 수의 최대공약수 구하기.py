a = input()
a = a.split()
cnt = 0
for i in range(1, int(a[0])+1) :
    if int(a[0]) % i == 0 :
        if int(a[1]) % i == 0 :
            cnt = i
print(cnt)