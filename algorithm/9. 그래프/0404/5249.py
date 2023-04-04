def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)
    rep[y] = find_set(x)


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    rep = [i for i in range(V+1)]
    graph = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph.append((u, v, w))

    graph.sort(key=lambda x: x[2])

    s = 0
    cnt = 0

    for u, v, w in graph:
        if find_set(u) != find_set(v):
            cnt += 1
            s += w
            union(u, v)
            if cnt == V:
                break

    print(f'#{test_case}', s)