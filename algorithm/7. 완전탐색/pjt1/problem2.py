def dfs(r, c, total):
    global minimum
    if total > minimum:
        return

    if r == n-1 and c == n-1:
        minimum = min(minimum, total)

    for d in [(1, 0), (0, 1)]:
        nr = r + d[0]
        nc = c + d[1]

        if 0 <= nr < n and 0 <= nc < n:
            new_total = total + arr[nr][nc]
            dfs(nr, nc, new_total)


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    minimum = 1e9

    dfs(0, 0, arr[0][0])

    print(f'#{test_case}', minimum)