T = int(input())
for test_case in range(1, T+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    start, end = map(int, input().split())
    visited = [0] * (v+1)
    visited[start] = 1
    queue = [start]

    while queue:
        a = queue.pop(0)
        if a == end:
            print(f'#{test_case}', visited[a] - 1)
            break

        for i in graph[a]:
            if not visited[i]:
                visited[i] = visited[a] + 1
                queue.append(i)

    else:
        print(f'#{test_case}', 0)