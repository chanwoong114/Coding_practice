from copy import deepcopy

def move(a, d, board):
    if d == 0:
        for i in range(a):
            cnt = 0
            for j in range(a - 1, -1, -1):
                if board[i][j]:
                    for jj in range(j + 1, a - cnt):
                        if board[i][j] == board[i][jj]:
                            board[i][j] = 0
                            board[i][jj] *= 2
                            cnt += 1
                            break

                        elif board[i][jj] and board[i][j] != board[i][jj]:
                            cnt += 1
                            save = board[i][j]
                            board[i][j] = 0
                            board[i][jj - 1] = save
                            break

                        elif jj == a - cnt - 1:
                            save = board[i][j]
                            board[i][j] = 0
                            board[i][jj] = save

    elif d == 1:
        for i in range(a):
            cnt = 0
            for j in range(a):
                if board[i][j]:
                    for jj in range(j - 1, -1 + cnt, -1):
                        if board[i][j] == board[i][jj]:
                            board[i][j] = 0
                            board[i][jj] *= 2
                            cnt += 1
                            break

                        elif board[i][jj] and board[i][j] != board[i][jj]:
                            cnt += 1
                            save = board[i][j]
                            board[i][j] = 0
                            board[i][jj + 1] = save
                            break

                        elif jj == cnt:
                            save = board[i][j]
                            board[i][j] = 0
                            board[i][jj] = save

    elif d == 2:
        for i in range(a):
            cnt = 0
            for j in range(a - 1, -1, -1):
                if board[j][i]:
                    for jj in range(j + 1, a - cnt):
                        if board[j][i] == board[jj][i]:
                            board[j][i] = 0
                            board[jj][i] *= 2
                            cnt += 1
                            break

                        elif board[jj][i] and board[j][i] != board[jj][i]:
                            cnt += 1
                            save = board[j][i]
                            board[j][i] = 0
                            board[jj-1][i] = save
                            break

                        elif jj == a - cnt - 1:
                            save = board[j][i]
                            board[j][i] = 0
                            board[jj][i] = save

    elif d == 3:
        for i in range(a):
            cnt = 0
            for j in range(a):
                if board[j][i]:
                    for jj in range(j - 1, -1 + cnt, -1):
                        if board[j][i] == board[jj][i]:
                            board[j][i] = 0
                            board[jj][i] *= 2
                            cnt += 1
                            break

                        elif board[jj][i] and board[j][i] != board[jj][i]:
                            cnt += 1
                            save = board[j][i]
                            board[j][i] = 0
                            board[jj + 1][i] = save
                            break

                        elif jj == cnt:
                            save = board[j][i]
                            board[j][i] = 0
                            board[jj][i] = save

def dfs(a, d, lst):
    global v
    lst1 = deepcopy(lst)
    move(n, d, lst1)

    if a == 5:
        for k in lst1:
            v = max(v, max(k))
        return

    for k in range(4):
        dfs(a+1, k, lst1)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
v = 0

for ii in range(4):
    arr1 = deepcopy(arr)
    dfs(1, ii, arr1)

print(v)

