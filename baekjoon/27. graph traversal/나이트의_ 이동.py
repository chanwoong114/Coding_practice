from collections import deque

def bfs(a, b, c, d):
    queue = deque()
    queue.append((a, b))
    board[a][b] = 1
    while queue:
        x, y = queue.popleft()

        if x == c and y == d:
            print(board[x][y] - 1)
            break

        for i in [(2, -1), (1, -2), (2, 1), (1, 2), (-2, 1), (-1, 2), (-2, -1), (-1, -2)]:
            nx = x + i[0]
            ny = y + i[1]

            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    board = [[0] * n for _ in range(n)]
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    bfs(a, b, c, d)