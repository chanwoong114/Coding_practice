import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

v, e, start = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [0] * (v+1)
cnt = 1

def dfs(a):
    global cnt
    visited[a] = cnt
    graph[a].sort(reverse=True)
    for i in graph[a]:
        if not visited[i]:
            cnt += 1
            dfs(i)

dfs(start)

for i in range(1, v+1):
    print(visited[i])