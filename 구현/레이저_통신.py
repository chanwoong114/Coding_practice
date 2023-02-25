from collections import deque

m, n = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
C = []
queue = deque()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'C':
            C.append((i, j))


queue.append(C[0])
visited[C[0][0]][C[0][1]] = 1
end = C[1]

def bfs():
    while queue:
        x, y = queue.popleft()
        if (x, y) == C[1]:
            print(visited[x][y] - 2)
            break

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            while 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == '*':
                    break
                if visited[nx][ny] > visited[x][y]+1 or not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

                nx += dx[k]
                ny += dy[k]

bfs()