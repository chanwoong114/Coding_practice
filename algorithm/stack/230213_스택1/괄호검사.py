T = int(input())
for test_case in range(1, 1+T):
    s = list(map(str, input().rstrip()))
    stack = []
    res = 0

    for i in s:
        if i == '(':
            stack.append(0)
        elif i == '{':
            stack.append(1)

        elif i == ')':
            if stack == [] or stack.pop() != 0:
                res = 1
                break
        elif i == '}':
            if stack == [] or stack.pop() != 1:
                res = 1
                break

    if res or stack:
        res = 0
    else:
        res = 1

    print(f'#{test_case}', res)