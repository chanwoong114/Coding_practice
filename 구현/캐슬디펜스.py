from collections import deque
from copy import deepcopy


def enemy_move():
    for i in range(N - 1, 0, -1):
        for j in range(M):
            board2[i][j] = board2[i - 1][j]
    for j in range(M):
        board2[0][j] = 0


def find_enemy(r, c):
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1
    check = []
    queue = deque()
    queue.append((r, c))

    if board2[r][c] == 1:
        return [r, c]

    while queue:
        x, y = queue.popleft()
        for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx = x + d[0]
            ny = y + d[1]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                if visited[nx][ny] > D:
                    if not check:
                        return 0
                    check.sort(key=lambda x: (x[2], x[1]))
                    return [check[0][0], check[0][1]]
                if board2[nx][ny]:
                    check.append((nx, ny, visited[nx][ny]))

    if not check:
        return 0

    check.sort(key=lambda x: (x[2], x[1]))

    return [check[0][0], check[0][1]]


def play_game(archer):
    global board2
    global max_count
    cnt = 0
    board2 = deepcopy(board)
    for _ in range(N):
        temp = []
        for i in archer:
            temp.append(find_enemy(N-1, i))
        for i in temp:
            if not i:
                continue
            if board2[i[0]][i[1]]:
                board2[i[0]][i[1]] = 0
                cnt += 1

        enemy_move()

    if cnt > max_count:
        max_count = cnt


def archer_arrange(k, res):
    if k == 3:
        play_game(res)
        return

    for i in range(M):
        if not archer_visit[i]:
            archer_visit[i] = 1
            res.append(i)
            archer_arrange(k+1, res)
            res.pop()
            archer_visit[i] = 0


N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
board2 = []
archer_visit = [0] * M
max_count = 0

archer_arrange(0, [])

print(max_count)
