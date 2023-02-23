T = int(input())
for test_case in range(1, T+1):
    n, m, l = map(int, input().split())
    tree = [0] * (n+1)

    for _ in range(m):
        v, e = map(int, input().split())
        tree[v] = e

    if n%2==0:
        tree[n//2] = tree[n]
        for i in range(n-2, 1, -2):
            tree[i//2] = tree[i] + tree[i+1]
    else:
        for i in range(n-1, 1, -2):
            tree[i // 2] = tree[i] + tree[i + 1]


    print(f'#{test_case}', tree[l])
