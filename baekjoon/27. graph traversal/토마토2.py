from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

m, n, h = map(int, input().split())
queue = deque()
board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 1:
                queue.append((i, j, k))

def bfs():
    while queue:
        z, x, y = queue.popleft()
        for a in range(6):
            nz = z + dz[a]
            nx = x + dx[a]
            ny = y + dy[a]

            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and board[nz][nx][ny] == 0:
                board[nz][nx][ny] = board[z][x][y] + 1
                queue.append((nz, nx, ny))

bfs()
cnt = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 0:
                print(-1)
                exit()
            if cnt < board[i][j][k]:
                cnt = board[i][j][k]

print(cnt-1)
