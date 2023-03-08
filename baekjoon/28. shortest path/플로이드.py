import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = []
distance = [[1e9] * n for i in range(n)]
for _ in range(m):
    v, e, d = map(int, input().split())
    if distance[v - 1][e - 1] > d:
        distance[v - 1][e - 1] = d

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

for i in distance:
    for j in i:
        if j == 1e9:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()