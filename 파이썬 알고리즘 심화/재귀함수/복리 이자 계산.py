def qhrfl(b):
    global c
    c *= (1+(b*0.01))

a = input()
a = a.split()
b = float(a[0])
c = int(a[1])
d = int(a[2])

for i in range(d):
    qhrfl(b)
print(c)