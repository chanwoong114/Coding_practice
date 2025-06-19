from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b, c):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = 1

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == c:
                visited[nx][ny] = 1
                queue.append((nx, ny))


n = int(input())
board = [list(map(str, input().strip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

cnt1 = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, board[i][j])
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            board[i][j] = 'R'

cnt2 = 0
visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, board[i][j])
            cnt2 += 1

print(cnt1, cnt2)

