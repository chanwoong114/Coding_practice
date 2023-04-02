def per(k, S):
    global minV
    if S > minV:
        return
    if k == n:
        minV = min(minV, S)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            per(k+1, S + arr[k][i])
            visited[i] = 0

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0]*n
    minV = 1e9

    per(0, 0)
    print(f'#{test_case}', minV)