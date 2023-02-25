from collections import deque

n, m = map(int, input().split())
visited = [0] * 101
start = []
end = []

for _ in range(n + m):
    s, e = map(int, input().split())
    start.append(s)
    end.append(e)

queue = deque([1])
visited[1] = 1

while queue:
    x = queue.popleft()

    for i in range(1, 7):
        nx = x + i

        if nx >= 100:
            if not visited[100] or visited[100] > visited[x] + 1:
                visited[100] = visited[x] + 1
            break

        for k in range(n+m):
            if nx == start[k]:
                nx = end[k]

        if visited[nx] > visited[x] + 1 or visited[nx] == 0:
            visited[nx] = visited[x] + 1
            queue.append(nx)

print(visited[100] - 1)