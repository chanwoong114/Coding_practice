def dfs(k, cnt):
    visited[k] = cnt
    for i in graph[k]:
        if not visited[i]:
            dfs(i, cnt)


T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for i in range(m):
        graph[lst[2*i]].append(lst[2*i+1])
        graph[lst[2*i+1]].append(lst[2*i])

    cnt = 1
    for j in range(1, n+1):
        if not visited[j]:
            dfs(j, cnt)
            cnt += 1

    print(f'#{test_case}', cnt-1)