from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    cnt = 2
    queue = deque()
    queue.append(s)
    visited[s] = 1
    while queue:
        x = queue.popleft()
        graph[x].sort()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = cnt
                cnt += 1
                queue.append(i)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)

visited = [0] * (n+1)

bfs(r)

for i in range(1, n+1):
    print(visited[i])