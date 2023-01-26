import sys
graph = []
blank = []

for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

def rowcheck(x, a):
    for i in range(9):
        if graph[x][i] == a:
            return False
    return True

def colcheck(y, a):
    for i in range(9):
        if graph[i][y] == a:
            return False
    return True

def boxcheck(x, y, a):
    nx = x//3*3
    ny = y//3*3

    for i in range(3):
        for j in range(3):
            if graph[nx+i][ny+j] == a:
                return False
    return True

def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)
    
    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if rowcheck(x, i) and colcheck(y, i) and boxcheck(x, y, i):
            graph[x][y] = i
            dfs(idx + 1)
            graph[x][y] = 0

dfs(0)