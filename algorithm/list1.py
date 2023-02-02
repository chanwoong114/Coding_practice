T = int(input())
for test_case in range(1, T+1):
    k, n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    oil = [0]*(n+1)
    distance = k
    count = 0
    check = distance

    for i in lst:
        oil[i] = 1

    while distance < n:
        if oil[distance]:
            count += 1
        else:
            while not oil[distance]:
                distance -= 1
                if check == distance:
                    count = -1
                    break
            if count == -1:
                break
            count += 1
        check = distance
        distance += k
    if count > 0:
        print(f'#{test_case} {count}')
    else:
        print(f'#{test_case} 0')