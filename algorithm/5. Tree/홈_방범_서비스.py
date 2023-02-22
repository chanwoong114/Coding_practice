from collections import deque

def bfs(x, y):
    cnt = board[x][y]
    queue = deque()
    visited = [[0]*n for _ in range(n)]
    queue.append((x, y))
    visited[x][y] = 1
    level = 1
    area = 1
    while queue:
        x, y = queue.popleft()

        if visited[x][y] == level:
            if cnt*m - area >= 0:
                res.append(cnt)
            area += level * 4
            level += 1

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                cnt += board[nx][ny]
                queue.append((nx, ny))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    home = 0

    for i in range(n):
        for j in range(n):
            res = []
            bfs(i, j)
            if res:
                count = max(res)
                if home < count:
                    home = count


    print(f'#{test_case}', home)