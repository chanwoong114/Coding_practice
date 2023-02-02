from collections import deque

n, k = map(int, input().split())
s = deque([])
print('<', end='')

for i in range(1, n+1):
    s.append(i)

for i in range(n-1):
    for j in range(k-1):
        a = s.popleft()
        s.append(a)
    a = s.popleft()
    print(a, end=', ')
a = s.popleft()
print(a, end='')
print('>')
