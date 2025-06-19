from collections import deque
import sys

input = sys.stdin.readline

def bfs(a):
    queue = deque()
    queue.append(a)
    visited[a] = 1

    while queue:
        na = queue.popleft()

        for k in graph[na]:
            if not visited[k]:
                queue.append(k)
                visited[k] = 1


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)