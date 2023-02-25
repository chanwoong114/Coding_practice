import sys
input = sys.stdin.readline

n = int(input())

board = [[0] * 1001 for _ in range(1001)]
for k in range(1, n+1):
    s1, s2, e1, e2 = map(int, input().split())
    for i in range(s1, s1+e1):
        for j in range(s2, s2+e2):
            board[i][j] = k

for k in range(1, n+1):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if board[i][j] == k:
                cnt += 1

    print(cnt)
