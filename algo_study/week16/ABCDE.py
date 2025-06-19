def dfs(k, d):
    global check

    if d == 5:
        check = 1
        return

    for i in graph[k]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, d+1)
            visited[i] = 0


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
check = 0

for _ in range(m):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)


visited = [0] * n
for j in range(n):
    visited[j] = 1
    dfs(j, 1)
    visited[j] = 0
    if check:
        break

print(check)