n, m = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(n)]

size = 0

for i in range(min(n, m)):
    for j in range(n-i):
        for k in range(m-i):
            if board[j][k] == board[j+i][k] == board[j][k+i] == board[j+i][k+i]:
                size = (i+1)**2

print(size)