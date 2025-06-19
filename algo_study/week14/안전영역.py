from collections import deque

def bfs(a, b, d):
    visited[a][b] = 1
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()

        for k in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + k[0]
            ny = y + k[1]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] > d:
                queue.append((nx, ny))
                visited[nx][ny] = 1


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
max_cnt = 0


for i in range(100):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for l in range(n):
            if not visited[j][l] and board[j][l] > i:
                bfs(j, l, i)
                cnt += 1

    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)