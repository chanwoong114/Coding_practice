n = int(input())
for i in range(n):
    s = list(str(input()))
    stack = []
    for i in s:
        if i == '(':
            stack.append(1)
        else:
            if len(stack):
                stack.pop()
            else:
                stack.append(1)
                break
    if len(stack):
        print('NO')
    else:
        print('YES')