n = int(input())
weight = list(map(int, input().split()))
m = int(input())
glass = list(map(int, input().split()))

dp = [[0 for j in range((i+1)*500+1)] for i in range(n+1)]

def cal(num, w):
    if num > n:
        return
    if dp[num][w]:
        return

    dp[num][w] = 1

    cal(num+1, w)
    cal(num+1, w+weight[num-1])
    cal(num+1, abs(w-weight[num-1]))

cal(0, 0)

for i in glass:
    if i > 15000:
        print('N', end=' ')
    elif dp[n][i] == 1:
        print('Y', end=' ')
    else:
        print('N', end=' ')