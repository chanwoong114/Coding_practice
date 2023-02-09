T = int(input())
check = [0] * 1000
check[0], check[1] = 1, 1
for i in range(2, int(1000**.5)+1):
    if check[i] == 0:
        for j in range(2 * i, 1000, i):
            check[j] = 1
sosu = []
for i in range(1000):
    if check[i] == 0:
        sosu.append(i)

for test_case in range(1, T+1):
    n = int(input())
    cnt = 0

    for i in range(len(sosu)):
        for j in range(i, len(sosu)):
            for k in range(j, len(sosu)):
                if sosu[i]+sosu[j]+sosu[k] == n:
                    cnt += 1

    print(f'#{test_case}', cnt)