from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for test_case in range(1, T+1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    high = 0
    for i in range(n):
        for j in range(n):
            if high < board[i][j]:
                high = board[i][j]

    def bfs(a, b, c, d, e):
        visited = [[[[] for _ in range(n)] for _ in range(n)] for _ in range(2)]
        queue = deque()
        queue.append((a, b, c, d))
        visited[0][a][b].append((a, b))

        while queue:
            x, y, z, h = queue.popleft()
            for ii in range(4):
                nx = x + dx[ii]
                ny = y + dy[ii]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if board[nx][ny] < h and (nx, ny) not in visited[z][x][y]:
                    if len(visited[z][x][y]) >= len(visited[z][nx][ny])-1:
                        visited[z][nx][ny] = []
                        for abc in visited[z][x][y]:
                            visited[z][nx][ny].append(abc)
                        visited[z][nx][ny].append((nx, ny))
                        queue.append((nx, ny, z, board[nx][ny]))

                if board[nx][ny] - e < h and z == 0:
                    if (nx, ny) not in visited[z][x][y]:
                        if len(visited[0][x][y]) >= len(visited[1][nx][ny]):
                            visited[1][nx][ny] = []
                            for abc in visited[0][x][y]:
                                visited[1][nx][ny].append(abc)
                            visited[1][nx][ny].append((nx, ny))
                            queue.append((nx, ny, 1, board[nx][ny]-e))

        return visited

    def len_check():
        max_len = 0
        for aaa in range(2):
            for bbb in range(n):
                for ccc in range(n):
                    if len(visited[aaa][bbb][ccc]) > max_len:
                        max_len = len(visited[aaa][bbb][ccc])

        return max_len

    res = 0
    for i in range(n):
        for j in range(n):
            for ll in range(1, k+1):
                if board[i][j] == high:
                    visited = bfs(i, j, 0, high, ll)
                    a = len_check()
                    if res < a:
                        res = a

    print(f'#{test_case}', res)