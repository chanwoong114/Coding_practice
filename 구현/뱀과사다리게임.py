def bfs(s):
    q = [s]
    visited = [0] * 101
    visited[s] = 1

    while q:
        i = q.pop(0)
        for j in range(1, 7):
            if i + j < 101 and visited[i + j] == 0:
                if i + j == 100:
                    return visited[i]
                if lst[i + j] != 0 and not visited[lst[i + j]]:
                    q.append(lst[i + j])
                    visited[lst[i + j]] = visited[i] + 1

                if lst[i + j] == 0:
                    q.append(i + j)
                    visited[i + j] = visited[i] + 1


N, M = map(int, input().split())
lst = [0] * 101

for _ in range(N + M):
    v1, v2 = map(int, input().split())
    lst[v1] = v2

print(bfs(1))
