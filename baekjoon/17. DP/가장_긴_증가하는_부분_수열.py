# DP 문제 이므로 수열사용해서 푼다
# 

n = int(input())
L = list(map(int, input().split()))
dp = [0]*n

for i in range(n):
    for j in range(n):
        if L[i]>L[j] and dp[i]<dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))