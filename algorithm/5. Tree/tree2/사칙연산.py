def cal(v1, v2, o):
    if o == '+':
        return v1 + v2
    elif o == '-':
        return v1 - v2
    elif o == '*':
        return v1 * v2
    else:
        return v1 // v2


for test_case in range(1, 11):
    n = int(input())
    tree = [[] for _ in range(n + 1)]
    dic = {}
    res = []
    for _ in range(n):
        lst = list(map(str, input().split()))
        if lst[1].isdigit():
            dic[int(lst[0])] = int(lst[1])
        else:
            dic[int(lst[0])] = lst[1]

        if len(lst) > 2:
            tree[int(lst[0])].append(int(lst[2]))
        if len(lst) == 4:
            tree[int(lst[0])].append(int(lst[3]))


    def inorder(n):
        if tree[n]:
            inorder(tree[n][0])
        if tree[n]:
            inorder(tree[n][1])
        res.append(dic[n])
        if res[-1] == '+' or res[-1] == '-' or res[-1] == '*' or res[-1] == '/':
            o = res.pop()
            v2 = res.pop()
            v1 = res.pop()
            res.append(cal(v1, v2, o))


    inorder(1)

    print(f'#{test_case}', res[0])
