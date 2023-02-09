from collections import deque
import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 0

for i in range(n):
    graph.append(list(map(int, input().split())))

def bfs():
    queue = deque()
    arr = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx>0 or nx>=n or ny<0 or ny>=m:
                continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = 2
                queue.append((nx, ny))
    
    global answer
    cnt = 0
    for i in range(n):
        cnt += arr[i].count(0)
    
    answer = max(answer, cnt)

def makeWall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0

makeWall(0)
print(answer)