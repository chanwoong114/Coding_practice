T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    code = [str(input()) for _ in range(n)]
    k = 0
    dic = {'1011000': 0,
           '1001100': 1,
           '1100100': 2,
           '1011110': 3,
           '1100010': 4,
           '1000110': 5,
           '1111010': 6,
           '1101110': 7,
           '1110110': 8,
           '1101000': 9,
           }

    c = []
    for i in range(n):
        k = 0
        code[i] = code[i][::-1]
        while k < m:
            if code[i][k] == '1':
                c.append(dic[code[i][k:k + 7]])
                k += 7
            else:
                k += 1

        if c:
            break

    check = 0
    for i in range(len(c)):
        if i%2:
            check += c[i] * 3
        else:
            check += c[i]

    print(f'#{test_case}', end=' ')

    if check%10:
        print(0)
    else:
        print(sum(c))