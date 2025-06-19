from collections import deque

n, m = map(int, input().split())

ans = []
yo = deque([i for i in range(1, n+1)])

cnt = 1
while yo:
    x = yo.popleft()
    if cnt % m == 0:
        ans.append(x)
    else:
        yo.append(x)
    cnt += 1

print('<', end='')
for i in range(n-1):
    print(ans[i], end=', ')
print(ans[n-1], end='')
print('>')