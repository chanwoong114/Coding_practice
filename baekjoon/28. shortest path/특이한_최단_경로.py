import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    v, e, d = map(int, input().split())
    graph[v].append((d, e))
    graph[e].append((d, v))

v1, v2 = map(int, input().split())

q = []

def dijkstra(s):
    global n
    distance = [1e9] * (n+1)
    distance[s] = 0
    heapq.heappush(q, (0, s))
    while q:
        dist, nn = heapq.heappop(q)

        for w, nnn in graph[nn]:
            cost = dist + w
            if cost < distance[nnn]:
                distance[nnn] = cost
                heapq.heappush(q, (cost, nnn))

    return distance

start = dijkstra(1)
d1 = dijkstra(v1)
d2 = dijkstra(v2)

cnt = min(start[v1] + d1[v2] + d2[n], start[v2] + d2[v1] + d1[n])

print(cnt if cnt < 1e9 else -1)
