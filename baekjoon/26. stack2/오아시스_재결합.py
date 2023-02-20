n = int(input())
arr = [int(input()) for _ in range(n)]

stack = []
res = 0

for i in arr:
    while stack and stack[-1][0] < i:
        res += stack.pop()[1]

    if not stack:
        stack.append((i, 1))
        continue

    if stack[-1][0] == i:
        cnt = stack.pop()[1]
        res += cnt

        if stack:
            res += 1
        stack.append((i, 1))
        res += 1

print(res)