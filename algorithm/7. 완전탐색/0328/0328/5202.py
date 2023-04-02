T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    time = [list(map(int, input().split())) for _ in range(n)]
    time.sort(key=lambda x: x[1])

    cnt = 1
    end = time[0][1]
    for i in range(1, n):
        if time[i][0] >= end:
            cnt += 1
            end = time[i][1]

    print(f'#{test_case}', cnt)