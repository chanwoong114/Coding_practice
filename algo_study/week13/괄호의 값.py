s = list(str(input()).strip())

stack = []
cnt = 0

for i in range(len(s)):
    if s[i] == '(' or s[i] == '[':
        stack.append([s[i], 0])

    elif s[i] == ')':
        if stack == [] or stack[-1][0] != '(':
            print(0)
            exit(0)
        b, n = stack.pop()
        if stack:
            if stack[-1][0] == '(':
                if n:
                    stack[-1][1] += 2*n
                else:
                    stack[-1][1] += 4
            else:
                if n:
                    stack[-1][1] += 3 * n
                else:
                    stack[-1][1] += 6
        else:
            if n:
                cnt += n
            else:
                cnt += 2

    elif s[i] == ']':
        if stack == [] or stack[-1][0] != '[':
            print(0)
            exit(0)
        b, n = stack.pop()
        if stack:
            if stack[-1][0] == '(':
                if n:
                    stack[-1][1] += 2 * n
                else:
                    stack[-1][1] += 6
            else:
                if n:
                    stack[-1][1] += 3 * n
                else:
                    stack[-1][1] += 9
        else:
            if n:
                cnt += n
            else:
                cnt += 3

print(cnt)
