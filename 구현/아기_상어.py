from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            a, b = i, j

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

size = 2
