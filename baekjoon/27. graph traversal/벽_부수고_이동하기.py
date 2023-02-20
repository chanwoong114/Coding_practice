from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a, b, c):
    queue = deque()
    queue.append((a, b, c))
    while queue:
        x, y, z = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if board[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0]