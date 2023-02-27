T = int(input())
for test_case in range(1, T+1):
    a = float(input())
    ans = ''

    for k in range(-1, -13, -1):
        if a >= 2**k:
            a -= 2**k
            ans += '1'
        else:
            ans += '0'

        if a == 0:
            print(f'#{test_case}', ans)
            break

    else:
        print(f'#{test_case}', 'overflow')
