import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [[0]*(M+1)] + [[0]+list(input().strip()) for _ in range(N)]

check_W = ['0'*(M+1)] + ['0' + 'WB'*(M//2) + 'W'*(M%2), '0' + 'BW'*(M//2) + 'B'*(M%2)]*(N//2) + ['0' + 'WB'*(M//2) + 'W'*(M%2)]*(N%2)
check_B = ['0'*(M+1)] + ['0' + 'BW'*(M//2) + 'B'*(M%2), '0' + 'WB'*(M//2) + 'W'*(M%2)]*(N//2) + ['0' + 'BW'*(M//2) + 'B'*(M%2)]*(N%2)

sum_W = [[0]*(M+1) for _ in range(N+1)]
sum_B = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        sum_W[i][j] = int(board[i][j] != check_W[i][j]) + sum_W[i-1][j] + sum_W[i][j-1] - sum_W[i-1][j-1]
        sum_B[i][j] = int(board[i][j] != check_B[i][j]) + sum_B[i-1][j] + sum_B[i][j-1] - sum_B[i-1][j-1]


result = float('inf')
for i in range(N-K+1):
    for j in range(M-K+1):
        x = i+K
        y = j+K

        count_W = sum_W[x][y] - sum_W[i][y] - sum_W[x][j] + sum_W[i][j]
        count_B = sum_B[x][y] - sum_B[i][y] - sum_B[x][j] + sum_B[i][j]

        result = min(result, count_W, count_B)

print(result)