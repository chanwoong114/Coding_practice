T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    cost = list(map(int, input().split()))
    count = 0
    buy = 0
    sell = 0

    for i in range(n):
        diff = 0
        for j in range(i+1, n):
            if cost[i] < cost[j]:
                diff = 1
                break
        if diff:
            count += 1
            buy += cost[i]
        else:
            sell += (count * cost[i]) - buy
            count = 0
            buy = 0

    print(f'#{test_case} {sell}')