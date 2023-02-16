T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dx = [0,0,1,-1,1,-1,1,-1]
    dy = [1,-1,0,0,1,1,-1,-1]

    max_cnt = 0

    for i in range(n):
        for j in range(m):
            cnt = 0
            x, y = i, j
            for d in range(8):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < n and 0 <= ny < m and board[x][y] > board[nx][ny]:
                    cnt += 1

            if cnt >= 4:
                max_cnt += 1

    print(f'#{test_case}', max_cnt)