from collections import deque

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)

def dfs(s):
    res = [s]
    st = []
    visited = [0] * (n+1)
    st.append(s)
    visited[s] = 1
    while st:
        x = st[-1]
        graph[x].sort()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                res.append(i)
                st.append(i)
                break
        else:
            st.pop()

    return res

def bfs(s):
    res = [s]
    queue = deque()
    visited = [0] * (n+1)
    queue.append(s)
    visited[s] = 1
    while queue:
        x = queue.popleft()
        graph[x].sort()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                res.append(i)
                queue.append(i)

    return res

d = dfs(r)
b = bfs(r)

print(*d)
print(*b)