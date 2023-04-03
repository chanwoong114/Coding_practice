from collections import deque

def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = 1

    while queue:
        a = queue.popleft()

        for i in [a-1, a+1, a*2, a-10]:
            if 0 < i <= 1000000 and not visited[i]:
                if i == m:
                    print(f'#{test_case}', visited[a])
                    return
                queue.append(i)
                visited[i] = visited[a] + 1


T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    visited = [0] * 1000001

    bfs(n)