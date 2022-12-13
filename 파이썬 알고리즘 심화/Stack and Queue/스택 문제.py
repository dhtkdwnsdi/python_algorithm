N = int(input())
stack = []
for i in range(N):
    a = input()
    if a[:4] == 'push':
        stack.append(int(a[5:]))
    elif a[:3] == 'pop':
        if stack == []: print(-1)
        else :
            print(stack[-1])
            stack.pop()
    elif a[:4] == 'size':
        print(len(stack))
    elif a[:5] == 'empty':
        if len(stack) == 0: print(1)
        else: print(0)
    elif a[:3] == 'top':
        if stack == []: print(-1)
        else: print(stack[-1])