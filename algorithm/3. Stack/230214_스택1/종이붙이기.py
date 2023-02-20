dp = [0]*31
dp[1] = 1

for i in range(2, 31):
    if i%2:
        dp[i] = dp[i-1]*2 - 1
    else:
        dp[i] = dp[i-1]*2 + 1

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    n //= 10
    print(f'#{test_case}', dp[n])