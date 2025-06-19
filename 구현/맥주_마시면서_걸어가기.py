from collections import deque

T = int(input())

for _ in range(T):
    n = int(input())
    graph = [[] for _ in range(n+2)]
    location = []

    for i in range(n+2):
        location.append(list(map(int, input().split())))

        for j in range(i):
            graph[j].append((i, abs(location[j][0] - location[i][0]) + abs(location[j][1] - location[i][1])))
            graph[i].append((j, abs(location[j][0] - location[i][0]) + abs(location[j][1] - location[i][1])))

    queue = deque()
    queue.append(0)

    visited = [0] * (n+2)
    visited[0] = 1

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if i[1] <= 1000 and not visited[i[0]]:
                queue.append(i[0])
                visited[i[0]] = 1


    if visited[n+1]:
        print('happy')
    else:
        print('sad')