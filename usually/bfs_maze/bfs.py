graph = []
f = open('input.txt', 'r')
for i in range(0, 101):
    line = f.readline()
    if i >=1:
        graph.append(list(line))
f.close()

for i in range(100):
    del graph[i][100]
    for j in range(100):
        graph[i][j] = int(graph[i][j])


from collections import deque
for _ in range(10):
    t = int(input())

    # graph = []
    
    # graph = [list(str(input())) for _ in range(100)]
        
    for i in range(100):
        for j in range(100):
            graph[i][j] = int(graph[i][j])
            if graph[i][j] == 2:
                ax, ay = i, j
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    c=0
    visit = [[False]*100 for _ in range(100)]
    queue = deque()
    queue.append((ax, ay))
    visit[ax][ay] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if x<0 or x>=100 or y<0 or y>=100:
                continue
            if graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                if not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
            
            if graph[nx][ny] == 3:
                c += 1
                break
        
    print(f'#{t} {c}')