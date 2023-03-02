dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

turn = [(),
        (1, 3, 0, 2),
        (1, 3, 2, 0),
        (2, 0, 3, 1),
        (3, 2, 0, 1),
        (2, 3, 0, 1)]


def play(a, b):
    for d in range(4):
        na = a + dx[d]
        nb = b + dy[d]
        if na < 0 or na >= n or nb < 0 or nb >= n:
            continue

        cnt = 0
        while True:
            if board[na][nb] == -1 or (na == a and nb == b):
                res.append(cnt)
                break
            if na == -1 or na == n or nb == -1 or nb == n:
                d = (d + 2) % 4
                cnt += 1

            if 1 <= board[na][nb] <= 5:
                cnt += 1
                d = turn[board[na][nb]][d]

            if board[na][nb] > 5:
                na, nb = dic[(na, nb)]

            na += dx[d]
            nb += dy[d]

        res.append(cnt)


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = []

    white = [[] for _ in range(11)]
    dic = {}
    for i in range(n):
        for j in range(n):
            if board[i][j] > 5:
                white[board[i][j]].append((i, j))

    for i in range(6, 11):
        if white[i]:
            dic[white[i][0]] = white[i][1]
            dic[white[i][1]] = white[i][0]
    print(dic)

    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                play(i, j)

    print(max(res))