from collections import deque

n, m = map(int, input().split())
lst = list(map(int, input().split()))

stack = deque(list(range(1, n+1)))
count = 0
b = len(stack)

for i in lst:
    a = stack.index(i)+1
    b = len(stack)
    if a == 1:
        stack.popleft()
    elif b-a+1 < a-1:
        count += b-a+1
        for i in range(b-a+1):
            stack.appendleft(stack.pop())
        stack.popleft()
    else:
        count += a-1
        for i in range(a-1):
            stack.append(stack.popleft())
        stack.popleft()

print(count)