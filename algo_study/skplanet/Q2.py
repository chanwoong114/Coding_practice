
from collections import deque
def solution(p, b):
    graph = [[] for _ in range(len(p))]
    for i in range(len(p)):
        if p[i] > 0:
            graph[p[i]].append(i)

    answer = []
    def bfs(s):
        cnt = 1
        visited = [0]*len(p)
        queue = deque()
        queue.append(s)
        visited[s] = 0
        while queue:
            x = queue.popleft()
            for i in graph[x]:
                if not visited[i]:
                    visited[i] = 1
                    cnt += 1
                    queue.append(i)
        return cnt

    for i in b:
        if p[i] == -1:
            answer.append(bfs(i))
        else:
            answer.append(0)

    return answer




print(solution([2, 2, -1, 1, 5, -1, 5], [2, 5]))
print(solution([2, 2, -1, 1, 5, -1, 5], [1, 5]))