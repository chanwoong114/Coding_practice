from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())
for _ in range(T):
    n, m, k = map(int, input().split())
    board = [[0]*n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1
    count = 0

    def bfs(a, b):
        queue = deque()
        queue.append((a, b))

        while queue:
            v, e = queue.popleft()
            for i in range(4):
                nx = v + dx[i]
                ny = e + dy[i]

                if 0 <= nx < m and 0 <= ny < n and board[nx][ny]:
                    board[nx][ny] = 0
                    queue.append((nx, ny))

    def dfs(a, b):
        board[a][b] = 0

        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]

            if 0 <= na < m and 0 <= nb < n and board[na][nb]:
                dfs(na, nb)

    for row in range(m):
        for col in range(n):
            if board[row][col] == 1:
                bfs(row, col)
                count += 1

    print(count)