def check(arr):
    visited = [0] * n
    for i in range(n):
        for j in [1, -1]:
            ni = i + j
            if ni < 0 or ni >= n:
                continue
            if arr[ni] >= arr[i]:
                continue
            if arr[i] - arr[ni] > 1:
                return False

            for q in range(k):
                if ni < 0 or ni >= n:
                    return False
                if arr[i] - arr[ni] == 1 and not visited[ni]:
                    visited[ni] = 1
                    ni += j
                else:
                    return False
    return True

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for ii in range(n):
    if check(board[ii]):
        cnt += 1
board = list(zip(*board[::-1]))
for ii in range(n):
    if check(board[ii]):
        cnt += 1

print(cnt)