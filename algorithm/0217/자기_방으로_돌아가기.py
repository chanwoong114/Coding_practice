T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    res = [0]*201
    for i in range(n):
        a, b = map(int, input().split())
        a=(a+1)//2
        b=(b+1)//2
        if a>b:
            a, b = b, a
        for j in range(a, b+1):
            res[j] += 1

    print(f'#{test_case}', max(res))
