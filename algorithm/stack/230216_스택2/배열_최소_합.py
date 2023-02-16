def per(res, k):
    global min_sum
    if k > min_sum:
        return
    if len(res) == n:
        if k < min_sum:
            min_sum = k
        return

    for i in range(n):
        if not visit[i]:
            visit[i] = True
            res.append(i)
            k += arr[i][len(res)-1]
            per(res, k)
            k -= arr[i][len(res) - 1]
            res.pop()
            visit[i] = False



T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [False] * n
    min_sum = 1e9
    per([], 0)
    print(f'#{test_case}', min_sum)


