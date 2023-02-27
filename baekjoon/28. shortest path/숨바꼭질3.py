from collections import deque

n, k = map(int, input().split())

graph = [[] for _ in range(100001)]
visited = [0] * 100001
for i in range(100001):
    graph[i].append((1, i-1))
    graph[i].append((1, i+1))
    graph[i].append((0, i*2))

def bfs():
    queue = deque()
    queue.append(n)
    visited[n] = 1
    while queue:
        x = queue.popleft()
        if x == k:
            return visited[k] - 1
        for w, j in graph[x]:
            if 0 <= j < 100001:
                if not visited[j] or visited[j] > visited[x] + w:
                    visited[j] = visited[x] + w
                    queue.append(j)

print(bfs())