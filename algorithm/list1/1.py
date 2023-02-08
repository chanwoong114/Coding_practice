T = int(input())
for test_case in range(1, T+1):
    s = str(input())
    res = 0
    if s == s[::-1]:
        res = 1

    print(f'#{test_case}', res)