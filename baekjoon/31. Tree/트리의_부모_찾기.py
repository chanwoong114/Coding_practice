import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)

visited = [0]*(n+1)

def dfs(s):
    for i in graph[s]:
        if not visited[i]:
            visited[i] = s
            dfs(i)

dfs(1)

for x in range(2, n+1):
    print(visited[x])