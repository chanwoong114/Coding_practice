T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    total = 0

    for i in range(m):
        maxV = 0
        for j in range(n):
            if truck[i] >= container[j]:
                if maxV < container[j]:
                    container[j], maxV = maxV, container[j]

        total += maxV

    print(f'#{test_case}', total)