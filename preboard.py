tc = int(input())

for test_case in range(1, tc + 1):

    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    sumV = []
    total = []
    row = []
    s = 0

    maxtotal = []

    if n == m:  # 정사각형일 때
        for i in range(n):
            for j in range(m):
                if i % 2 == 0:
                    total.append(arr[j][i])
                    s += arr[j][i]
            sumV.append(s)

    elif n < m: # m이 n보다 클 때
        for i in range(n + 1):
            for j in range(m - (m - n)):

                if i % 2 == 0:
                    total.append(arr[j][i])
                    s += arr[j][i]
            sumV.append(s)
    else: # n 이 m 보다 클 때
        for i in range(m):
            for j in range(n):
                if i % 2 == 0:
                    total.append(arr[j][i])
                    s += arr[j][i]
            sumV.append(s)

    for i in range(n):
        for j in range(m):
            if arr[i][j] == max(total) and j % 2 == 0:
                maxtotal.append(j)

    a, b, c, d = max(sumV), len(total), max(total), max(maxtotal) + 1
    print(f'#{test_case}', a, b, c, d)