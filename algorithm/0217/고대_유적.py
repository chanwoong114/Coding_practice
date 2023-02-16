T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    max_cnt = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            if board[i][j]:
                cnt += 1
            else:
                if max_cnt < cnt:
                    max_cnt = cnt
                cnt = 0
        if max_cnt < cnt:
            max_cnt = cnt

    for j in range(m):
        cnt = 0
        for i in range(n):
            if board[i][j]:
                cnt += 1
            else:
                if max_cnt < cnt:
                    max_cnt = cnt
                cnt = 0
        if max_cnt < cnt:
            max_cnt = cnt

    print(f'#{test_case}', max_cnt)