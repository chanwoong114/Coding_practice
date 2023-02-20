board = [list(map(int, input().split())) for _ in range(5)]
order = [list(map(int, input().split())) for _ in range(5)]
visit = [[0]*5 for _ in range(5)]
cnt = 0

def find(a):
    for k in range(5):
        for l in range(5):
            if a == board[k][l]:
                visit[k][l] = 1
                return


def check():
    global cnt

    cross1 = 0
    cross2 = 0
    for k in range(5):
        rcnt = 0
        ccnt = 0
        for l in range(5):
            if visit[k][l] == 1:
                rcnt += 1
            if visit[l][k] == 1:
                ccnt += 1

        if visit[k][k] == 1:
            cross1 += 1
        if visit[k][4-k] == 1:
            cross2 += 1

        if rcnt == 5:
            cnt += 1
        if ccnt == 5:
            cnt += 1

    if cross1 == 5:
        cnt += 1
    if cross2 == 5:
        cnt += 1


def bingo():
    global cnt
    count = 0
    for i in range(5):
        for j in range(5):
            count += 1
            find(order[i][j])
            check()
            if cnt >= 3:
                return count
            cnt = 0

print(bingo())