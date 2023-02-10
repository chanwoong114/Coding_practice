import sys
input = sys.stdin.readline

di = [0,0,1,-1]
dj = [1,-1,0,0]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
maxValue = 0

def dfs(i, j, value, cnt):
    global maxValue

    if cnt == 4:
        maxValue = max(maxValue, value)
        return

    for x in range(4):
        ni = i + di[x]
        nj = j + dj[x]

        if 0<=ni<n and 0<=nj<m and not visited[ni][nj]:
            visited[ni][nj] = 1
            dfs(ni, nj, value+board[ni][nj], cnt+1)
            visited[ni][nj] = 0

def exec(i, j):
    global maxValue

    for x in range(4):
        value = board[i][j]

        for y in range(3):
            d = (x+y)%4
            ni = i + di[d]
            nj = j + dj[d]

            if ni<0 or ni>=n or nj<0 or nj>=m:
                value = 0
                break

            value += board[ni][nj]

        maxValue = max(maxValue, value)

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, board[i][j], 1)
        visited[i][j] = 0
        exec(i,j)

print(maxValue)
