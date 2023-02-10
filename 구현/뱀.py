import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())
board = [[0]*n for _ in range(n)]
visit = [[0]*n for _ in range(n)]
m = int(input())
for i in range(m):
    row, col = map(int, input().split())
    board[row-1][col-1] = 1
td = []
k = int(input())
for k in range(k):
    t, d = map(str, input().split())
    td.append((int(t), d))
td.append((0, 0))
timer = 0
x, y = 0, 0
d = 0
body = [[0, 0], [0, 0]]

while True:
    block = 0
    nx = x + dx[d]
    ny = y + dy[d]
    timer += 1

    if nx < 0 or nx >= n or ny < 0 or ny >= n or visit[nx][ny] == 1:
        break

    body[0][0], body[0][1] = nx, ny
    a, b = body[-1][0], body[-1][1]

    for i in range(len(body)-1, 0, -1):
        visit[body[i][0]][body[i][1]] = 0
        body[i][0], body[i][1] = body[i-1][0], body[i-1][1]

    if board[nx][ny] == 1:
        body.append([a, b])
        board[nx][ny] = 0

    for i in range(1, len(body)):
        visit[body[i][0]][body[i][1]] = 1

    if td[0][0] == timer:
        if td[0][1] == 'D':
            d = (d+1) % 4
        elif td[0][1] == 'L':
            d = (d+3) % 4
        td.pop(0)

    x = nx
    y = ny

print(timer)