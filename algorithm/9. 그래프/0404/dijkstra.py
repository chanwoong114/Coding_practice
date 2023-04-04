'''
5 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

# def dijkstra(s):    # s : 출발
#     U = [0] * (V+1) # U : 최소 비용이 결정된 정점 집합
#     U[s] = 1        # U = {s}
#
#     for i in range(V+1):
#         D[i] = adjM[s][i]
#
#     # 남은 정점의 비용 결정 while U != V
#     N = V+1 # N개의 정점
#     for _ in range(N-1):   # N-1개 정점의 비용 결정
#         # D[w]가 최소인 w 결정
#         minV = INF
#         w = 0
#         for i in range(N):
#             if U[i] == 0 and minV > D[i]:   # 남은 정점 i 중, 최소
#                 w = i
#                 minV = D[i]
#
#         U[w] = 1    # 최소인 w는 최소 비용 D[w] 확정
#         # w에 인접인 정점에 대해, 기존 비용 vs w를 거쳐가는 비용
#         for v in range(V+1):
#             if 0 < adjM[w][v] < INF:    # w에 인접인 v의 조건
#                 D[v] = min(D[v], D[w] + adjM[w][v])
#
# INF = 10000     # 문제에 따라 조절 대략 1e9
# V, E = map(int, input().split())    # 0~V 번 정점, E : 간선 수
# adjM = [[INF] * (V+1) for _ in range(V+1)]
# for i in range(V+1):
#     adjM[i][i] = 0
#
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     adjM[u][v] = w
#
# D = [0] * (V+1)
#
# dijkstra(0)
# print(D)

def dijkstra():
    U = []
    D = [1e9] * V
    D[0] = 0

    while len(U) < V:
        # 1. D중 제일 작은 v를 선택
        minV = 1e9
        for i in range(V):
            if i in U: continue
            if minV > D[i]:
                minV = D[i]
                v = i
        # 2. U에 v를 추가
        U.append(v)

        # 3. D를 갱신
        for w in range(V):
            if w in U: continue
            if G[v][w]:
                D[w] = min(D[w], G[v][w] + D[v])

    print(U)
    print(D)


V, E = map(int, input().split())
V += 1
G = [[0] * V for _ in range(V)]

for _ in range(E):
    v1, v2, w = map(int, input().split())
    G[v1][v2] = w

dijkstra()