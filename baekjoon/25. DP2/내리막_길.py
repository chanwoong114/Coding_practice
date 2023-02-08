import sys
input = sys.stdin.readline

def dfs(x, y):
    # 도착 도달하면 1을 리턴
    if x == n-1 and y == m-1:
        return 1

    # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴
    if dp[x][y] != -1:
        return dp[x][y]
    
    ways = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<m and graph[x][y] > graph[nx][ny]:
            ways += dfs(nx, ny)
    
    dp[x][y] = ways
    return dp[x][y]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

print(dfs(0,0))