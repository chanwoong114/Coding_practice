import sys
input = sys.stdin.readline

s = list(map(str, input().rstrip()))
key = list(map(str, input().rstrip()))
n = len(key)
stack = []

for i in s:
    if i == key[-1] and len(stack) >= n-1:
        if n == 1:
            continue
        if stack[-(n-1):] == key[0:n-1]:
            for _ in range(n-1):
                stack.pop()
        else:
            stack.append(i)
    else:
        stack.append(i)

if stack:
    print(''.join(stack))
else:
    print('FRULA')