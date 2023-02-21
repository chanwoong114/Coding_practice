dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().rstrip())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                queue = [(i, j)]

    def dfs():
        while queue:
            x, y = queue.pop(0)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 > nx or nx >= n or 0 > ny or ny >= n:
                    continue
                if board[nx][ny] == 3:
                    print(f'#{test_case}', visited[x][y])
                    return

                if not board[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

        print(f'#{test_case}', 0)
        return

    dfs()