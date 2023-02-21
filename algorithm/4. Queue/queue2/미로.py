dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for test_case in range(1, 11):
    n = int(input())
    board = [list(map(int, input().rstrip())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    queue = [(1, 1)]
    stack = [(1, 1)]
    visited[1][1] = 1

    # def bfs():
    #     while queue:
    #         x, y = queue.pop(0)
    #
    #         for i in range(4):
    #             nx = x + dx[i]
    #             ny = y + dy[i]
    #
    #             if board[nx][ny] == 3:
    #                 print(f'#{test_case}', 1)
    #                 return
    #             if not board[nx][ny] and not visited[nx][ny]:
    #                 visited[nx][ny] = 1
    #                 queue.append((nx, ny))
    #     print(f'#{test_case}', 0)
    #     return
    # bfs()
    def dfs():
        while stack:
            x, y = stack.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if board[nx][ny] == 3:
                    print(1)
                    return
                if board[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    stack.append((nx, ny))

        print(0)
        return
    dfs()


    def dfs(x, y):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if board[nx][ny] == 3:
                print(1)
                return
            if board[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                dfs(nx, ny)

        print(0)
        return


    dfs()