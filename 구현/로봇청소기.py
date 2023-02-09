from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dr = [-1,0,1,0]
dc = [0,1,0,-1]

visit = [[0]*m for _ in range(n)]
visit[r][c] = 1
cnt = 1

while True:
    flag = 1
    for _ in range(4):
        d = (d+3)%4
        nr = r + dr[d]
        nc = c + dc[d]

        if 0<=nr<n and 0<=nc<m and arr[nr][nc] == 0:
            if visit[nr][nc] == 0:
                visit[nr][nc] = 1
                r = nr
                c = nc
                cnt += 1
                flag = 0
                break

    if flag:
        if arr[r-dr[d]][c-dc[d]] == 1:
            print(cnt)
            break
        else:
            r = r-dr[d]
            c = c-dc[d]