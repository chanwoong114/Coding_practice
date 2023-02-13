for test_case in range(1, 11):
    t = int(input())
    n, m = map(int, input().split())

    def power(m):
        if m == 1:
            return n

        return power(m-1)*power(1)

    print(f'#{t}', power(m))