n, m = map(int, input().split())
search = int(input())
board = [[0]*m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0
x, y = 0, 0
board[x][y] = 1
if search == 1:
    print(1, 1)
if n * m >= search:
    for i in range(2, search+1):
        nx = x + dx[d]
        ny = y + dy[d]

        if nx<0 or nx>=n or ny<0 or ny>=m or board[nx][ny]:
            d = (d+1)%4
            nx = x + dx[d]
            ny = y + dy[d]
        
        if search == i:
            print(nx+1, ny+1)
            break

        board[nx][ny] = i
        x = nx
        y = ny

else:
    print(0)