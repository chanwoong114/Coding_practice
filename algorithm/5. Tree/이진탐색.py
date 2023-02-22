T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    tree = [[] for _ in range(n+1)]
    cnt = 1
    def inorder(r):
        global cnt
        if r < len(tree):
            inorder(r*2)
            tree[r] = cnt
            cnt += 1
            inorder(r*2 + 1)

    inorder(1)

    print(f'#{test_case}', tree[1], tree[n//2])

