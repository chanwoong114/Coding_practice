from collections import deque
import sys
input = sys.stdin.readline


def bfs(a, b):
    global size
    queue = deque()
    queue.append((a, b))
    visited = [[0] * n for _ in range(n)]
    visited[a][b] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] > size:
                continue
            if board[nx][ny] != 0 and board[nx][ny] < size and not visited[nx][ny]:
                res.append((visited[x][y], nx, ny))
                visited[nx][ny] = visited[x][y] + 1
            if not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    if res:
        return 1
    else:
        return 0

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            a, b = i, j
board[a][b] = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

size = 2
eat = 0
res = []
cnt = 0

while bfs(a, b):
    res.sort(key = lambda x : (x[0], x[1], x[2]))
    a, b = res[0][1], res[0][2]
    board[a][b] = 0
    cnt += res[0][0]

    res = []
    eat += 1
    if size == eat:
        size += 1
        eat = 0

print(cnt)