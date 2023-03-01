def check1(a, b):
    sumV = 0
    sumV += board[a][b]
    for k in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        na = a + k[0]
        nb = b + k[1]
        c = 1
        while 0 <= na < n and 0 <= nb < n and c < m:
            sumV += board[na][nb]
            na += k[0]
            nb += k[1]
            c += 1
    return sumV
def check2(a, b):
    sumV = 0
    sumV += board[a][b]
    for k in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
        na = a + k[0]
        nb = b + k[1]
        c = 1
        while 0 <= na < n and 0 <= nb < n and c < m:
            sumV += board[na][nb]
            na += k[0]
            nb += k[1]
            c += 1
    return sumV


T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    value = []

    for i in range(n):
        for j in range(n):
            value.append(check1(i, j))
            value.append(check2(i, j))

    print(f'#{test_case}', max(value))

