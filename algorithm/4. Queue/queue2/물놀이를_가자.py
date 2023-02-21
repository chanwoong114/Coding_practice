from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    board = [list(map(str, input().rstrip())) for _ in range(n)]
    cnt = 0
    queue = deque()
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'W':
                queue.append((i, j))


    def bfs():
        for a, b in queue:
            visited[a][b] = 1

        while queue:
            x, y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    bfs()

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'L':
                cnt += (visited[i][j] - 1)


    print(f'#{test_case}', cnt)