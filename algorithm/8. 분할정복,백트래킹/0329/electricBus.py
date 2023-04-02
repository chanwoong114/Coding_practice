T = int(input())
for test_case in range(1, T+1):
    lst = list(map(int, input().split()))
    dp = [10000] * (lst[0]+1)
    dp[lst[0]] = 0
    dp[lst[0]-1] = 1

    for i in range(lst[0]-2, 0, -1):
        check = min(i + lst[i], lst[0])
        for j in range(i, check+1):
            dp[i] = min(dp[i], dp[i + 1] + 1, 1 + dp[j])

    print(f'#{test_case}', dp[1]-1)