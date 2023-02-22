from collections import deque


def bfs(x, y):
    cnt = 1
    visited[x][y] = 1
    board[x][y] = 0
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for k in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + k[0]
            ny = y + k[1]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny]:
                cnt += 1
                visited[nx][ny] = 1
                board[nx][ny] = 0
                queue.append((nx, ny))

    res.append(cnt)

n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
res = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            bfs(i, j)

print(len(res))
for i in sorted(res):
    print(i)