from collections import deque

def bfs():
    queue = deque()
    queue.append(1)
    board[1] = 1
    while queue:
        x = queue.popleft()
        for k in range(1, 7):
            nx = x + k
            if dic.get(nx, 0):
                nx = dic[nx]
            if nx == 100:
                print(board[x])
                return

            if nx < 101 and not board[nx]:
                board[nx] = board[x] + 1
                queue.append(nx)



n, m = map(int, input().split())
board = [0] * 101
dic = {}

for i in range(n+m):
    a, b = map(int, input().split())
    dic[a] = b

bfs()