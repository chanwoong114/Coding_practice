from copy import deepcopy

def move(a, d, board):
    flag = 0
    if d == 0:
        for i in range(a):
            for j in range(a-1, 0, -1):
                if not board[i][j] or board[i][j] == board[i][j-1]:
                    board[i][j] += board[i][j-1]
                    board[i][j-1] = 0
                    flag = 1

    elif d == 1:
        for i in range(a):
            for j in range(a-1):
                if not board[i][j] or board[i][j] == board[i][j+1]:
                    board[i][j] += board[i][j+1]
                    board[i][j+1] = 0
                    flag = 1

    elif d == 2:
        for i in range(a):
            for j in range(a-1, 0, -1):
                if not board[j][i] or board[j][i] == board[j-1][i]:
                    board[j][i] += board[j-1][i]
                    board[j-1][i] = 0
                    flag = 1

    elif d == 3:
        for i in range(a):
            for j in range(a-1):
                if not board[j][i] or board[j][i] == board[j+1][i]:
                    board[j][i] += board[j+1][i]
                    board[j+1][i] = 0
                    flag = 1

    return flag, board

def dfs(a, d, lst):
    global v
    flag, lst1 = move(n, d, lst)
    if not flag:
        return

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
    dfs(1, ii, arr)

print(v)