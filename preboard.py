from copy import deepcopy
import sys
from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def per(idx):
    global maxV
    if idx == 3:
        Q = deque()
        for a in range(N):
            for b in range(M):
                if original_map[a][b] == 2:
                    Q.append((a, b))
        virus(Q)
        return

    for i in range(N):
        for j in range(M):
            if original_map[i][j] == 0:
                original_map[i][j] = 1
                per(idx+1)
                original_map[i][j] = 0

def virus(Q):
    global maxV
    visited = [[False] * M for _ in range(N)]

    while Q:
        x, y = Q.popleft()
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < N and 0 <= nj < M and original_map[ni][nj] == 0 and visited[ni][nj] == False:
                Q.append((ni, nj))
                visited[ni][nj] = True

    cnt = 0
    for c in range(N):
        for d in range(M):
            if original_map[c][d] == 0 and visited[c][d] == False:
                cnt += 1
    maxV = max(maxV, cnt)

# def virus(i, j, new_map):
#     Q = deque()
#     Q.append((i, j))
#     visited[i][j] = True
#
#     while Q:
#         x, y = Q.popleft()
#         for k in range(4):
#             ni = x + di[k]
#             nj = y + dj[k]
#             if 0 <= ni < N and 0 <= nj < M and new_map[ni][nj] == 0:
#                 new_map[ni][nj] = 2
#                 Q.append((ni, nj))
#                 visited[ni][nj] = True


N, M = map(int, sys.stdin.readline().split())
original_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lst = []
per_lst = []
maxV = 0

per(0)

print(maxV)