from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

queue = deque()
queue.append((0, 0))
visited[0][0] = 1

while queue:
    x, y = queue.popleft()
    if x == n-1 and y == m-1:
        print(visited[x][y])
        break
    for i in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx = x + i[0]
        ny = y + i[1]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny]:
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))
