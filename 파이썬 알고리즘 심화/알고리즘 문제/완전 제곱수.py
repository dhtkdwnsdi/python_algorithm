a = int(input())
cnt = 0
for i in range(a) :
    b = int(input())
    for j in range(1, b+1) :
        if j*j == b :
            cnt+=1
            break
print(cnt)