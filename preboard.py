import sys
from collections import deque
def check(contry_i, contry_j):
    global day
    Q = deque([])
    Q.append((contry_i, contry_j))
    visited[contry_i][contry_j] = cnt
    while Q:
        c_i, c_j = Q.popleft()
        contry = A[c_i][c_j]
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            new_i = c_i + di
            new_j = c_j + dj
            if 0<= new_i < N and 0<= new_j < N and visited[new_i][new_j] == 0:
                if L <= abs(contry - A[new_i][new_j]) <= R:
                    Q.append((new_i, new_j))
                    visited[new_i][new_j] = cnt

def cal():
    total = [0] * (cnt)
    total_count = [0] * (cnt)

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                total[visited[i][j]] += A[i][j]
                total_count[visited[i][j]] += 1

    for i in range(1, cnt):
        if total_count:
            total[i] //= total_count[i]

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                A[i][j] = total[visited[i][j]]



N, L, R = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
day = 0

while True:
    visited = [[0]*N for _ in range(N)]
    cnt = 1
    for i in range(N):
        for j in range(N):
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if 0 <= i + di < N and 0 <= j + dj < N and visited[i][j] == 0:
                    if L <= abs(A[i][j] - A[i + di][j + dj]) <= R:
                        check(i, j)
                        cnt += 1

    if cnt == 1:
        break

    cal()
    day += 1

print(day)
