n, m = map(int, input().split())
arr = list(map(int, input().split()))

board = [['0'] * m for _ in range(n)]

for i in range(m):
    for j in range(arr[i]):
        board[n-1-j][i] = '1'

cnt = 0

for i in range(n):
    s = ''.join(board[i]).strip('0')
    cnt += s.strip().count('0')

print(cnt)