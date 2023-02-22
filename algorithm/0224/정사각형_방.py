
from collections import deque
def dfs(x, y):
    global cnt
    q = deque()
    q.append((x, y))
    cnt += 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] - board[x][y] == 1:
                    visited[nx][ny] = 1
                    cnt += 1
                    q.append((nx, ny))

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    res = []

    for i in range(n):
        for j in range(n):
            visited = [[0]*n for _ in range(n)]
            cnt = 0
            dfs(i, j)
            res.append((board[i][j], cnt))

    res.sort(key = lambda x : (-x[1], x[0]))

    print(f'#{test_case}', *res[0])

