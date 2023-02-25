from collections import deque

for test_case in range(1, 11):
    n, start = map(int, input().split())
    graph = [[] for _ in range(101)]
    visited = [0]*101
    lst = list(map(int, input().split()))

    for i in range(0, n, 2):
        graph[lst[i]].append(lst[i+1])

    def bfs(s):
        queue = deque()
        queue.append(s)
        visited[s] = 1

        while queue:
            x = queue.popleft()
            for i in graph[x]:
                if not visited[i]:
                    visited[i] = visited[x] + 1
                    queue.append(i)


    bfs(start)

    idx, count = 0, 0
    for i in range(100, 0, -1):
        if count < visited[i]:
            count = visited[i]
            idx = i

    print(f'#{test_case}', idx)