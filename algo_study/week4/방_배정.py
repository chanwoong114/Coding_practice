n, m = map(int, input().split())

grade = [[0]*2 for _ in range(6)]
for _ in range(n):
    s, g = map(int, input().split())
    grade[g-1][s] += 1

cnt = 0
for i in range(6):
    for j in range(2):
        cnt += (grade[i][j]-1)//m + 1

print(cnt)