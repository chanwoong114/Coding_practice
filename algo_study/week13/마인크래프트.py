def check(k):
    time = 0
    block = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] < k:
                time += k - board[i][j]
                block += k - board[i][j]

            else:
                time += 2 * (board[i][j] - k)
                block -= board[i][j] - k

    if block > b:
        return 1e10
    return time


n, m, b = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

min_time = 1e9
min_height = 0

for l in range(257):
    check_time = check(l)
    if min_time >= check_time:
        min_time = check_time
        min_height = l

print(min_time, min_height)
