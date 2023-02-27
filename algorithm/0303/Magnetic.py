for test_case in range(1, 11):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    for i in range(n):
        check = 0
        for j in range(n):
            if board[j][i] == 1:
                check = 1

            elif board[j][i] == 2 and check == 1:
                cnt += 1
                check = 0

    print(f'#{test_case}', cnt)
