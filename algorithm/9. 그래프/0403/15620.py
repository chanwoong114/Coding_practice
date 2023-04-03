import heapq

def dijkstra(n):
    dist = [[1e9]*n for _ in range(n)]
    pq = []
    heapq.heappush(pq, (0, (0, 0)))
    dist[0][0] = 0
    while pq:
        d, p = heapq.heappop(pq)

        for i in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = p[0] + i[0]
            ny = p[1] + i[1]
            if 0 <= nx < n and 0 <= ny < n:
                cost = d + 1 + max(0, board[nx][ny] - board[p[0]][p[1]])
                if cost < dist[nx][ny]:
                    dist[nx][ny] = cost
                    heapq.heappush(pq, (cost, (nx, ny)))

    return dist


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    minV = 1e9
    aa = dijkstra(n)
    print(f'#{test_case}', dijkstra(n)[n-1][n-1])