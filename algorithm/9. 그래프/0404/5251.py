import heapq

def dijkstra(s):
    queue = []
    dist[s] = 0
    heapq.heappush(queue, (0, s))
    while queue:
        d, x = heapq.heappop(queue)

        for nd, nx in graph[x]:
            cost = d + nd
            if cost < dist[nx]:
                dist[nx] = cost
                heapq.heappush(queue, (cost, nx))


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    dist = [1e9] * (V+1)

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append([w, v])

    dijkstra(0)
    print(f'#{test_case}', dist[V])