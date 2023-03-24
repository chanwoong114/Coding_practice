from collections import deque

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = 1
    while queue:
        x, y = queue.popleft()

        for k in [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx = x + k[0]
            ny = y + k[1]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny]:
                visited[nx][ny] = 1
                board[nx][ny] = 0
                queue.append((nx, ny))


while True:
    m, n = map(int, input().split())
    if not m and not n:
        break

    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)