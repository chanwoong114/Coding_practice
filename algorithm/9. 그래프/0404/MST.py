'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''


# def findset(x):  # x 가 속한 집합의 대표
#     while x != rep[x]:  # x == rep[x]까지
#         x = rep[x]
#     return x
#
#
# def union(x, y):  # y의 대표원소가 x의 대표원소를 가리키도록
#     rep[findset(y)] = findset(x)
#     rep[y] = findset(x)
#
#
# V, E = map(int, input().split())  # 0~V : 정점번호, E : 간선수
# # makeset()
#
# rep = [i for i in range(V + 1)]
#
# graph = []
# for _ in range(E):
#     v1, v2, w = map(int, input().split())
#     graph.append([v1, v2, w])
#
# # (1) 가중치 기준 오름차순 정렬
# graph.sort(key=lambda x: x[2])
#
# # (2) N개 정점(V+1), N-1개의 간선 선택
# s = 0   # MST에 포함된 간선의 가중치 합
# cnt = 0
# MST = []
# for u, v, w in graph:   # 가중치가 작은 것부터
#     if findset(u) != findset(v):    # 사이클이 생기지 않으면
#         cnt += 1
#         s += w  # 가중치 합
#         MST.append([u, v, w])
#         union(u, v)
#         if cnt == V:  # MST 구성 완료
#             break
# print(s)
# print(MST)

# Prim 알고리즘
def prim():
    U = []
    D = [1e9] * V
    S = [-1]*V

    D[1] = 0

    while len(U) < V:
        # 1. D에서 제일 작은 값인 index(v)를 찾는다.
        # U에 없는 v기준으로
        minV = 1e9
        for i in range(V):
            if i in U: continue
            if minV > D[i]:
                minV = D[i]
                v = i

        # 2. v를 U에 넣는다.
        U.append(v)

        # 3. v하고 연결된 w의 D값을 최선으로 수정한다.
        # U에 없는 v기준으로
        for w in range(V):
            if w in U: continue
            if g[v][w] and D[w] > g[v][w]:
                D[w] = g[v][w]
                S[w] = v
            # if g[v][w]:
            #     D[w] = min(D[w], g[v][w])

    print(D)
    print(U)
    print(S)

V, E = map(int, input().split())
V += 1
g = [[0]*V for _ in range(V)]
for _ in range(E):
    v1, v2, w = map(int, input().split())
    g[v1][v2] = w

prim()
print(g)