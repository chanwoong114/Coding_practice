import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(n-1):
    v, e, d = map(int, input().split())
    graph[v].append((e, d))
    graph[e].append((v, d))

def dfs(s):
    for i in graph[s]:
        if not visited[i[0]]:
            visited[i[0]] = visited[s] + i[1]
            dfs(i[0])


visited[1] = 1
dfs(1)

m = visited.index(max(visited))
visited = [0] * (n+1)
visited[m] = 1
dfs(m)

print(max(visited) - 1)

