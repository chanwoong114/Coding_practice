r = c = 100
board = [[0] * c for _ in range(r)]

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            board[i][j] = 1

cnt = 0

for i in range(r):
    for j in range(c):
        if board[i][j] == 1:
            cnt += 1

print(cnt)