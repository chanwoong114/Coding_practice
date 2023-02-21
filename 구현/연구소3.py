from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 1e9

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    global cnt
    queue = deque()
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                queue.append((i, j))
                visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and not board[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


    def min_count():
        count = 0
        for i in range(n):
            for j in range(n):
                if not board[i][j] and visited[i][j] - 1 > count:
                    count = visited[i][j] - 1
        return count

    cnt = min(cnt, min_count())


def per(a):
    global two
    if a == two - m:
        bfs()
        return

    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                board[i][j] = 3
                per(a+1)
                board[i][j] = 2

two = 0
for i in board:
    two += i.count(2)

per(0)

print(cnt)