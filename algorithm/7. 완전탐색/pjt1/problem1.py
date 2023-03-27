def per(res):
    global minimum
    if len(res) == n:
        res.append(0)
        sumV = 0
        for i in range(n):
            sumV += arr[res[i]][res[i + 1]]
        res.pop()
        minimum = min(minimum, sumV)
        return

    for i in range(1, n):
        if not visited[i]:
            visited[i] = 1
            res.append(i)
            per(res)
            res.pop()
            visited[i] = 0


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    minimum = 1e9

    per([0])
    print(f'#{test_case}', minimum)
