T = int(input())
for test_case in range(1, T+1):
    e, n = map(int, input().split())
    lst = list(map(int, input().split()))
    tree = [[] for _ in range(e+2)]

    for i in range(e):
        tree[lst[i*2]].append(lst[i*2+1])

    cnt = 0
    def preorder(n):
        global cnt
        cnt += 1
        if len(tree[n]):
            preorder(tree[n][0])
        if len(tree[n]) == 2:
            preorder(tree[n][1])

    preorder(n)

    print(f'#{test_case}', cnt)