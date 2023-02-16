n = int(input())

dp_cnt = 0
dp = [0]*n
dp[1] = 1
dp[0] = 1

for i in range(2, n):
    dp[i] = dp[i-1] + dp[i-2]
    dp_cnt += 1

print(dp[n-1], dp_cnt)