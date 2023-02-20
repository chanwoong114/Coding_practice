for test_case in range(1, 11):
    t = int(input())
    lst = list(map(int, input().split()))
    d = 0

    while True:
        d = (d + 1) % 5
        if not d:
            d = 5
        save = lst[0]
        for i in range(7):
            lst[i] = lst[i+1]

        if save - d > 0:
            save -= d
            lst[7] = save
        else:
            lst[7] = 0
            break

    print(f'#{test_case}', *lst)
