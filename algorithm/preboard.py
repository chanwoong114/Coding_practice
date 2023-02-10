T = int(input())
for test_case in range(1, T + 1):
    n, m, k, r, c = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    order = [list(map(int, input().split())) for _ in range(k)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    dust = lst[r][c]
    lst[r][c] = 0

    for i in order:
        d = i[0]
        for j in range(i[1]):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                if d%2:
                    d -= 1
                else:
                    d += 1
                nr = r + dr[d]
                nc = c + dc[d]

            dust += lst[nr][nc]
            lst[nr][nc] = 0

            r, c = nr, nc

    print(f'#{test_case}', dust, r, c)