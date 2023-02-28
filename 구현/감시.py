from copy import deepcopy

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dic = {1: [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]],
       2: [[(-1, 0), (1, 0)], [(0, 1), (0, -1)]],
       3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(-1, 0), (0, -1)]],
       4: [[(-1, 0), (0, -1), (0, 1)], [(-1, 0), (1, 0), (0, 1)], [(1, 0), (0, -1), (0, 1)],
           [(-1, 0), (1, 0), (0, -1)]],
       5: [[(1, 0), (-1, 0), (0, -1), (0, 1)]]}

queue = []
min_zero = 100

for i in range(n):
    for j in range(m):
        if board[i][j] in [1, 2, 3, 4, 5]:
            queue.append((i, j))

load = [[] for _ in range(len(queue))]

def count_zero():
    cnt = 0
    for aa in range(n):
        for bb in range(m):
            if board[aa][bb] == 0:
                cnt += 1
    return cnt


def dfs(a):
    global min_zero

    if a == len(queue):
        c = count_zero()
        if min_zero > c:
            min_zero = c
        return

    x = queue[a][0]
    y = queue[a][1]

    for k in dic[board[x][y]]:
        load[a] = []
        for l in k:
            nx = x + l[0]
            ny = y + l[1]
            while 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 6:
                if board[nx][ny] not in [1,2,3,4,5]:
                    load[a].append((nx, ny, board[nx][ny]))
                    board[nx][ny] = 9
                nx += l[0]
                ny += l[1]

        dfs(a + 1)
        for l in load[a]:
            board[l[0]][l[1]] = l[2]


dfs(0)

print(min_zero)
