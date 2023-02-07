n, m = map(int, input().split())
procession1 = [list(map(int, input().split())) for _ in range(n)]
a, b = map(int, input().split())
procession2 = [list(map(int, input().split())) for _ in range(a)]

lst = [[0]*b for _ in range(n)]


for i in range(n):
    for j in range(b):
        v = 0
        for k in range(m):
            v += procession1[i][k]*procession2[k][j]
            
        lst[i][j] += v
for i in lst:
    print(*i)