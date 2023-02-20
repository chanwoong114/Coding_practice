dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    global res
    visit[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if board[nx][ny] == 1 or visit[nx][ny] == 1:
            continue

        if board[nx][ny] == 3:
            res = 1
            return
        dfs(nx, ny)

def find(n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                x, y = i, j
                return x, y


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().rstrip())) for _ in range(n)]
    visit = [[0]*n for _ in range(n)]

    x, y = find(n)

    res = 0
    dfs(x, y)

    print(f'#{test_case}', res)