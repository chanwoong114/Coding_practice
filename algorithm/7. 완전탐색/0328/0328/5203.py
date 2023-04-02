def babygin(lst):
    if len(lst) < 3:
        return False
    c_lst = sorted(lst)
    for j in range(len(c_lst) - 2):
        if c_lst[j] == c_lst[j + 1] == c_lst[j + 2]:
            return True

    c_lst = list(set(c_lst))
    if len(c_lst) < 3:
        return False
    for j in range(len(c_lst) - 2):
        if c_lst[j] == c_lst[j + 1] - 1 == c_lst[j + 2] - 2:
            return True

    return False


T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    p1, p2 = [], []
    for i in range(12):
        if not i % 2:
            p1.append(arr[i])
            if babygin(p1):
                print(f'#{test_case}', 1)
                break
        else:
            p2.append(arr[i])
            if babygin(p2):
                print(f'#{test_case}', 2)
                break
    else:
        print(f'#{test_case}', 0)
