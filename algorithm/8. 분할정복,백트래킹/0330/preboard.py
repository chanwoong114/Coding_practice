def process(m, s):
    global res
    if res <= s:
        return
    if m > 12:
        res = min(res, s)
        return

    # if month:

T = int(input())
for test_case in range(1, T + 1):
    fee = list(map(int, input().split()))
    month = [0] + list(map(int, input().split()))
    dp = [0] * 13
    res = fee[3]

    for i in range(1, 13):
        dp[i] = min(dp[i - 1] + fee[1], fee[0] * month[i] + dp[i - 1])

        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + fee[2])

    print(f'#{test_case}', min(dp[12], fee[3]))
