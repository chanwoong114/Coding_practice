s = str(input())

stack = []
cnt = 0

for i in s:
    if i == '(':
        stack.append(1)
    else:
        a = stack.pop()
        if a == 1:
            for j in range(len(stack)):
                stack[j] += 1
        else:
            cnt += a

print(cnt)