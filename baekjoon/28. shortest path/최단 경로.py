import heapq
import sys

input = sys.stdin.readline

INF = 1e9

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
q = []

def dijkstra(s):
    distance[s] = 0
    heapq.heappush(q, (0, s))
    while q:
        dist, x = heapq.heappop(q)

        if distance[x] < dist:
            continue

        for w, nn in graph[x]:
            cost = dist + w
            if cost < distance[nn]:
                distance[nn] = cost
                heapq.heappush(q, (cost, nn))

for _ in range(m):
    v, e, d = map(int, input().split())
    graph[v].append((d, e))

dijkstra(start)

for i in range(1, n + 1):
    print("INF" if distance[i] == INF else distance[i])
