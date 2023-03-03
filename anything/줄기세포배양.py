from collections import deque
import sys
sys.stdin = open("sample_input.txt", "r")

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    board = [[0] * 351 for _ in range(351)]
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = deque()
    queue = deque()

    for i in range(150, 150 + n):
        for j in range(150, 150 + m):
            board[i][j] = arr[i - 150][j - 150]
            if arr[i - 150][j - 150]:
                res.append([arr[i - 150][j - 150], i, j])

    time_check = deque()
    for i in range(k):

        for _ in range(len(res)):
            t, x, y = res.popleft()
            if t > 0:
                res.append([t-1, x, y])
            else:
                queue.append([x, y])
                time_check.append(board[x][y])

        visited = []
        check = []
        while queue:
            x, y = queue.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if not board[nx][ny]:
                    visited.append((nx, ny, board[x][y]))

        for j in visited:
            if board[j[0]][j[1]] < j[2]:
                board[j[0]][j[1]] = j[2]
                check.append(j)

        for j in check:
            if board[j[0]][j[1]] == j[2]:
                res.append([j[2], j[0], j[1]])

        for _ in range(len(time_check)):
            a = time_check.popleft()
            if a > 1:
                time_check.append(a-1)

    print(f'#{test_case}', len(res) + len(time_check))