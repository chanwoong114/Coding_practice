N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key = lambda x:x[0])

dp = [0]*N

for i in range(N):
    for j in range(N):
        if lst[i][1] > lst[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(N-max(dp))