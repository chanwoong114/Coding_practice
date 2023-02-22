for test_case in range(1, 11):
    n = int(input())
    tree = [[] for _ in range(n+1)]
    dic = {}
    for i in range(n):
        lst = list(map(str, input().split()))
        dic[int(lst[0])] = lst[1]
        if len(lst) > 2:
            for j in range(2, len(lst)):
                tree[int(lst[0])].append(int(lst[j]))

    print(f'#{test_case}', end=' ')

    def inorder(n):
        if len(tree[n]):
            inorder(tree[n][0])
        print(dic[n], end='')
        if len(tree[n]) == 2:
            inorder(tree[n][1])

    inorder(1)
    print()
