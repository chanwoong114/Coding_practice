T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    triangle = []

    print(f'#{test_case}')
    for i in range(n):
        triangle.append(1)
        if i<2:
            pass
        else:
            for j in range(i-1, 0, -1):
                triangle[j] += triangle[j-1]
        print(*triangle)