from collections import deque

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = 1

    while queue:
        x, y = queue.popleft()
        if x == e[0] and y == e[1]:
            return visited[x][y] - 1

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

dx = [2, 1, 2, 1, -2, -1, -2, -1]
dy = [1, 2, -1, -2, 1, 2, -1, -2]
T = int(input())
for test_case in range(T):
    n = int(input())
    s = list(map(int, input().split()))
    e = list(map(int, input().split()))
    visited = [[0] * n for _ in range(n)]

    print(bfs(s[0], s[1]))
