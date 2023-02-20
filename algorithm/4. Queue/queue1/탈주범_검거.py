from collections import deque

T = int(input())
for test_case in range(1, T+1):
    n, m, r, c, t = map(int, input().split())
    dic = {1 : [(1, 0), (-1, 0), (0, 1), (0, -1)],
           2 : [(1, 0), (-1, 0)],
           3 : [(0, 1), (0, -1)],
           4 : [(-1, 0), (0, 1)],
           5 : [(1, 0), (0, 1)],
           6 : [(1, 0), (0, -1)],
           7 : [(-1, 0), (0, -1)]}
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]

    queue = deque()
    queue.append((r, c))
    visited[r][c] = 1
    time = 1
    ans = 1
    while queue:
        x, y = queue.popleft()
        if visited[x][y] == t:
            continue
        for k in dic[board[x][y]]:
            nx = x + k[0]
            ny = y + k[1]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny]:
                if (-k[0], -k[1]) in dic[board[nx][ny]]:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    ans += 1

    print(f'#{test_case}', ans)