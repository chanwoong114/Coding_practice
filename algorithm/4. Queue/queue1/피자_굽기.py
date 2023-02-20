T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    pit = []

    a = 1

    while True:
        if len(pit) < n:
            if queue:
                pit.append((queue.pop(0), a))
                a += 1
                continue
        save, save_index = pit.pop(0)
        save = save//2
        if save:
            pit.append((save, save_index))

        if len(pit) == 1:
            print(f'#{test_case}', pit[0][1])
            break