T = int(input())
for _ in range(T):
    s1, s2, e1, e2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        a, b, d = map(int, input().split())
        check = 0
        if ((a-s1)**2 + (b-s2)**2)**.5 <= d:
            check += 1
        if ((a - e1) ** 2 + (b - e2) ** 2) ** .5 <= d:
            check += 1
        if check == 1:
            cnt += 1
    print(cnt)



