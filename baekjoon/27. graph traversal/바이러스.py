from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)

cnt = 0
def bfs(s):
    global cnt
    queue = deque()
    queue.append(s)
    visited[s] = 1
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                cnt += 1
                queue.append(i)

bfs(1)

print(cnt)