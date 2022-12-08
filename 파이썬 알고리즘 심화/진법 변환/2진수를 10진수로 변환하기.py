a = input()
b = 0
c = 1
for i in a :
    b = b + (2**(len(a)-c))*int(i)
    c+=1
print(b)