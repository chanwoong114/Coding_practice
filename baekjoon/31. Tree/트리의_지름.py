import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    start, end, d = map(int, input().split())
    graph[start].append((end, d))
    graph[end].append((start, d))


def dfs(start):
    for i in graph[start]:
        if not visited[i[0]]:
            visited[i[0]] = visited[start] + i[1]
            dfs(i[0])


max_d = 0

visited = [0] * (n + 1)
visited[1] = 1
dfs(1)
d = max(visited) - 1
idx = visited.index(max(visited))
visited = [0] * (n + 1)
visited[idx] = 1
dfs(idx)
d = max(visited) - 1

print(d)