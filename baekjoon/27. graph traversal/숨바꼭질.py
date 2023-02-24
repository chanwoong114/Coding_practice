from collections import deque

n, k = map(int, input().split())

visited = [0] * 100001
def bfs(s):
    queue = deque()
    queue.append(s)
    while queue:
        x = queue.popleft()
        if x == k:
            print(visited[x])
            return
        for i in (x+1, x-1, x*2):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)

bfs(n)
