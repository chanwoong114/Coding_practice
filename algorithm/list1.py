def maximum(a, b):
    if a >= b:
        return a
    else:
        return b


for test_case in range(1, 11):
    a = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))

    max_sum = 0
    sum_diagonal1, sum_diagonal2 = 0, 0

    for i in range(100):
        sum_row = 0
        sum_col = 0
        sum_diagonal1 += arr[i][99 - i]
        sum_diagonal2 += arr[99 - i][i]

        for j in range(100):
            sum_row += arr[i][j]
            sum_col += arr[j][i]

        max_sum = maximum(max_sum, sum_row)
        max_sum = maximum(max_sum, sum_col)

    max_sum = maximum(max_sum, sum_diagonal1)
    max_sum = maximum(max_sum, sum_diagonal2)

    print(f'#{test_case} {max_sum}')