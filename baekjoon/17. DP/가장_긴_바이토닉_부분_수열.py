n = int(input())
L = list(map(int, input().split()))

dp = [0]*n
dp2 = [0]*n

for i in range(n):
    for j in range(n):
        if L[i] > L[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] +=1

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if L[i] > L[j] and dp2[i] < dp2[j]:
            dp2[i] = dp2[j]
    dp2[i] += 1

for i in range(n):
    dp[i] = dp[i] + dp2[i] - 1

print(max(dp))
