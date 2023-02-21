from collections import deque
import sys
sys.setrecursionlimit(10**6)

T = int(input())
for test_case in range(T):
    n, m, e = map(int, input().split())
    board = [[0]*n for _ in range(m)]
    for _ in range(e):
        x, y = map(int, input().split())
        board[y][x] = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    def bfs(a, b):
        queue = deque()
        queue.append((a, b))
        board[a][b] = 0

        while queue:
            v, e = queue.popleft()
            for i in range(4):
                nx = v + dx[i]
                ny = e + dy[i]

                if 0 <= nx < m and 0 <= ny < n and board[nx][ny]:
                    board[nx][ny] = 0
                    queue.append((nx, ny))
    def dfs(a, b):
        st = []
        st.append((a, b))
        board[a][b] = 0

        while st:
            x, y = st.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < m and 0 <= ny < n and board[nx][ny]:
                    board[nx][ny] = 0
                    st.append((nx, ny))

    def dfs2(a, b):
        board[a][b] = 0

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < m and 0 <= ny < n and board[nx][ny]:
                dfs2(nx, ny)


    count = 0
    for row in range(m):
        for col in range(n):
            if board[row][col] == 1:
                dfs2(row, col)
                count += 1
    print(count)