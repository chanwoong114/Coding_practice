n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
count = [0,0,0]

def dfs(x, y, n):
    check = lst[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != lst[i][j]:
                check = 2
    
    if check == 2:
        n = n//3
        dfs(x, y, n)
        dfs(x, y+n, n)
        dfs(x, y+2*n, n)
        dfs(x+n, y, n)
        dfs(x+n, y+n, n)
        dfs(x+n, y+2*n, n)
        dfs(x+2*n, y, n)
        dfs(x+2*n, y+n, n)
        dfs(x+2*n, y+2*n, n)

    elif check == -1:
        count[0] += 1
    elif check == 0:
        count[1] += 1
    else:
        count[2] += 1
        
dfs(0, 0, n)

for i in count:
    print(i)
