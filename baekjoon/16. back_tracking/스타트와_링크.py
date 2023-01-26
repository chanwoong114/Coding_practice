N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
minimum = int(1e9)

def dfs(depth, idx):
    global minimum
    if depth == N//2:
        team1, team2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    team1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    team2 += graph[i][j]
        minimum = min(minimum, abs(team1 - team2))
        return
    
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False

dfs(0, 0)
print(minimum)