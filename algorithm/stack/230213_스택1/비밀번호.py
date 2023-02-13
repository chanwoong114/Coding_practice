for test_case in range(1, 11):
    n, m = map(str, input().split())
    stack = []

    for i in m:
        if stack == []:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    print(f'#{test_case}', ''.join(stack))