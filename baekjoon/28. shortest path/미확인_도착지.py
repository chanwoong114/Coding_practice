import sys
from heapq import heappop, heappush
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        v, e, d = map(int, input().split())
        graph[v].append([e, d])
        graph[e].append([v, d])

    x = []
    for _ in range(t):
        x.append(int(input()))

    def dijkstra(start):
        heap = []
        heappush(heap, [0, start])
        distance = [1e9] * (n + 1)
        distance[start] = 0
        while heap:
            w, now = heappop(heap)
            for nn, weight in graph[now]:
                cost = weight + w
                if cost < distance[nn]:
                    distance[nn] = cost
                    heappush(heap, [cost, nn])


        return distance


    S = dijkstra(s)
    G = dijkstra(g)
    H = dijkstra(h)
    ans = []
    for i in x:
        if S[g] + G[h] + H[i] == S[i] or S[h] + H[g] + G[i] == S[i]:
            ans.append(i)

    ans.sort()
    print(*ans)