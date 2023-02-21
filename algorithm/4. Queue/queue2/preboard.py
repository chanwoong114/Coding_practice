# n = 7
# s = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
# graph = [[] for _ in range(n + 1)]
# lst = list(map(int, s.split()))
# for i in range(len(lst) // 2):
#     graph[lst[i * 2]].append(lst[2 * i + 1])
#     graph[lst[i * 2 + 1]].append(lst[2 * i])
#
# print(graph)
#
# queue = [1]
# visited = [0]*(n+1)
# visited[1] = 1
#
# while queue:
#     a = queue.pop(0)
#     print(a)
#
#     for i in graph[a]:
#         if not visited[i]:
#             visited[i] = 1
#             queue.append(i)
#
from collections import deque

def bfs(q):
    global road
    while q:
        t = q.popleft()
        road += t[2]
        for k in range(4):
            new_dy = t[0] + dy[k]
            new_dx = t[1] + dx[k]
            if 0 <= new_dx < M and 0 <= new_dy < N and not visited[new_dy][new_dx]:
                visited[new_dy][new_dx] = True
                q.append((new_dy, new_dx, t[2]+1))


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(str, input().rstrip())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    road = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(N):
        for j in range(M):
            if lst[i][j] == 'W':
                visited[i][j] = True
                queue.append((i, j, 0))

    bfs(queue)
    print(f'#{tc} {road}')
