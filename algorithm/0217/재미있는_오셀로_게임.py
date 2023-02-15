T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())

    board = [[0]*n for _ in range(n)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    board[n//2-1][n//2-1] = 2
    board[n//2-1][n//2] = 1
    board[n//2][n//2-1] = 1
    board[n//2][n//2] = 2

    for i in range(m):
        y, x, c = map(int, input().split())
        x -= 1
        y -= 1
        board[x][y] = c
        for d in range(4):
            cnt = 0
            nx = x + dx[d]
            ny = y + dy[d]
            while True:
                if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 0:
                    cnt = 0
                    break

                if board[nx][ny] != c:
                    cnt += 1
                else:
                    break

                nx += dx[d]
                ny += dy[d]


            for j in range(1, cnt+1):
                board[x+dx[d]*j][y+dy[d]*j] = c

        for k in [[1,1], [-1,-1], [1,-1], [-1,1]]:
            cnt = 0
            nx = x + k[0]
            ny = y + k[1]
            while True:
                if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 0:
                    cnt = 0
                    break

                if board[nx][ny] != c:
                    cnt += 1
                else:
                    break

                nx += k[0]
                ny += k[1]

            for j in range(1, cnt + 1):
                board[x + k[0] * j][y + k[1] * j] = c

    cnt_b, cnt_w = 0,0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt_b += 1
            elif board[i][j] == 2:
                cnt_w += 1

    print(f'#{test_case}', cnt_b, cnt_w)
