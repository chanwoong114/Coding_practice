T = int(input())

for test_case in range(1, T+1):
    lst = list(map(int, input()))
    count = 0

    for i in range(len(lst)-1, 0, -1):
        if lst[i] == lst[i-1]:
            pass
        else:
            count += 1

    if lst[0] == 1:
        count += 1

    print(f'#{test_case} {count}')