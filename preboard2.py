def honey(idx, jdx, res):
    global maxV, maxV1

    def max_honey(idx, cnt, S, r, lst):
        global maxV1
        if cnt > c:
            return
        if maxV1 < S:
            maxV1 = S
        if r == m:
            return

        for i in range(idx, m):
            max_honey(i + 1, cnt + lst[i], S + lst[i] ** 2, r + 1, lst)

    if len(res) == 2:
        maxV1 = 0
        lst1 = arr[res[0][0]][res[0][1]: res[0][1] + m]
        max_honey(0, 0, 0, 0, lst1)
        temp = maxV1
        maxV1 = 0
        lst2 = arr[res[1][0]][res[1][1]: res[1][1] + m]
        max_honey(0, 0, 0, 0, lst2)

        maxV = max(maxV, maxV1 + temp)



    for i in range(idx, n):
        for j in range(n - m + 1):
            if i == idx and j < jdx:
                continue

            res.append((i, j))
            honey(i, j + m - 1, res)
            res.pop()


T = int(input())
for test_case in range(1, T + 1):
    n, m, c = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    maxV = 0
    maxV1 = 0

    honey(0, 0, [])
    print(maxV)
