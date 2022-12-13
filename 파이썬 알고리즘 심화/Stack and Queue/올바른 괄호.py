def check(a):
    global stack
    global c
    if a == '(' :
        stack.append(a)
    else :
        if(stack == []):
            c = False
        else:
            stack.pop()

a = input()
stack = []
c = True

for i in a:
    check(i)

if len(stack) == 0 : print('true')
elif c == False : print('false')
else : print('false')


