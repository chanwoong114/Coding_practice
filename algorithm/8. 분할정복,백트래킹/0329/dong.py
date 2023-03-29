def per(k, S):
    global maxV
    if S < maxV:
        return

    if k == n:
        maxV = max(maxV, S)
        return

    for i in range(n):
        if not visited[i] and arr[k][i]:
            visited[i] = 1
            per(k+1, S * arr[k][i] / 100)
            visited[i] = 0

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0]*n
    maxV = 0

    per(0, 1)
    print(f'#{test_case}', '{:.6f}'.format(maxV*100))