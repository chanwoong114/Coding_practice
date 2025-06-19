import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(k, res, start):
    global result

    if res and start == k:
        for j in res:
            result.append(j)
        return

    for d in graph[k]:
        if not visited[d]:
            res.append(d)
            visited[d] = 1
            dfs(d, res, start)
            visited[d] = 0
            res.pop()

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    graph[i].append(int(input()))
result = []
visited = [0] * (n+1)

for i in range(1, n+1):
    if i not in result:
        dfs(i, [], i)

result.sort()

print(len(result), *result)