from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(T):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    dic = {1: 2, 2: 1}

    for _ in range(m):
        v, e = map(int, input().split())
        graph[v].append(e)
        graph[e].append(v)


    def bfs(s):
        queue = deque()
        queue.append(s)
        visited[s] = 1

        while queue:
            x = queue.popleft()

            for i in graph[x]:
                if not visited[i]:
                    visited[i] = dic[visited[x]]
                    queue.append(i)
                elif visited[i] == visited[x]:
                    return False

        return True

    for i in range(1, n+1):
        if not visited[i]:
            res = bfs(i)
            if not res:
                print('NO')
                break
    else:
        print('YES')