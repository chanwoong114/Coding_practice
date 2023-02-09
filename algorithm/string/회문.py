T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    lst = [list(map(str, input())) for _ in range(n)]
    ss = []

    for i in range(n):
        for j in range(n-m+1):
            count_row = 0
            count_col = 0
            for k in range(m//2):
                if lst[i][j+k] == lst[i][j+m-k-1]:
                    count_row += 1
                if lst[j+k][i] == lst[j+m-k-1][i]:
                    count_col += 1
            if count_row == m//2:
                s = "".join(lst[i][j:j+m])
            if count_col == m//2:
                for l in range(m):
                    ss.append(lst[j+l][i])
                s = "".join(ss)

    print(f'#{test_case}',s)