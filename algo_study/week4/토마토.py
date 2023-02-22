from collections import deque


m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
queue = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue.append((i, j))

def bfs():
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))

bfs()

d = 0
for i in range(n):
    for j in range(m):
        if not board[i][j]:
            print(-1)
            exit(0)
        if d < board[i][j]:
            d = board[i][j]
else:
    print(d-1)