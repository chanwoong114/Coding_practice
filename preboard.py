from collections import deque
from sys import stdin
def bfs(y, x):
    q = deque()
    q.append((y, x))
    lst[y][x] = 0
    while q:
        y, x = q.popleft()
        for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
            ndy = y + dy
            ndx = x + dx
            if 0 <= ndy < h and 0 <= ndx < w and lst[ndy][ndx] == 1:
                lst[ndy][ndx] = 0
                q.append((ndy, ndx))


while True:
    w, h = map(int, stdin.readline().split())
    if w == 0 and h == 0:
        break
    lst = [list(map(int, stdin.readline().split())) for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if lst[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)
