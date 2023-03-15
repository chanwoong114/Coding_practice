def roll(d):
    if d == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif d == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    elif d == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]


def location(x, y, d):
    k = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    return x + k[d - 1][0], y + k[d - 1][1]


n, m, r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
turn = list(map(int, input().split()))

dice = [0] * 6

for i in turn:
    roll(i)
    r, c = location(r, c, i)
    if 0 <= r < n and 0 <= c < m:
        if board[r][c]:
            dice[5] = board[r][c]
            board[r][c] = 0
        else:
            board[r][c] = dice[5]
        print(dice[0])
    else:
        if i % 2:
            roll(i+1)
            r, c = location(r, c, i+1)
        else:
            roll(i-1)
            r, c = location(r, c, i-1)
