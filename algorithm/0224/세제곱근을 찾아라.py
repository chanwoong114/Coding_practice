T = int(input())
for test_case in range(1, T+1):
    n = int(input())

    m = round(n**(1/3))

    if m**3 == n:
        print(f'#{test_case}', m)
    else:
        print(f'#{test_case}', -1)