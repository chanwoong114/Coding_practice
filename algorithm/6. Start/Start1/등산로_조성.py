from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for test_case in range(1, T+1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    def bfs(a, b, c):
        visited = [[[[] for _ in range(n)] for _ in range(n)] for _ in range(2)]
        queue = deque()
        queue.append((a, b, c))
        visited[0][a][b].append((a, b))

        while queue:
            x, y, z = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if board[nx][ny] > board[x][y] and (nx, ny) not in visited[z][x][y]:
                    if len(visited[z][x][y]) >= len(visited[z][nx][ny]):
                        visited[z][nx][ny] = []
                        for abc in visited[z][x][y]:
                            visited[z][nx][ny].append(abc)
                        visited[z][nx][ny].append((nx, ny))
                        queue.append((nx, ny, z))

                if board[nx][ny] + k > board[x][y] and z == 0:
                    if len(visited[0][x][y]) <= 1:
                        if (nx, ny) not in visited[z][x][y]:
                            if len(visited[1][x][y]) >= len(visited[0][nx][ny]):
                                visited[1][nx][ny] = []
                                for abc in visited[0][x][y]:
                                    visited[1][nx][ny].append(abc)
                                visited[1][nx][ny].append((nx, ny))
                                queue.append((nx, ny, 1))
                    elif board[visited[0][x][y][-2][0]][visited[0][x][y][-2][1]] < board[x][y] - k:
                        if (nx, ny) not in visited[z][x][y]:
                            if len(visited[1][x][y]) >= len(visited[0][nx][ny]):
                                visited[1][nx][ny] = []
                                for abc in visited[0][x][y]:
                                    visited[1][nx][ny].append(abc)
                                visited[1][nx][ny].append((nx, ny))
                                queue.append((nx, ny, 1))
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
            visited = bfs(i, j, 0)
            for ac in visited:
                for bc in ac:
                    print(*bc)
            print()
            a = len_check()
            if res < a:
                res = a

    print(f'#{test_case}', res)