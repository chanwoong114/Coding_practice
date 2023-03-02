def cal(v1, v2, o1):
    if o1 == '+':
        return v1 + v2
    elif o1 == '-':
        return v1 - v2
    elif o1 == '*':
        return v1 * v2
    elif o1 == '/':
        return int(v1 / v2)

def dfs(res, a):
    global min_ans, max_ans
    if a == n-1:
        c = nums.copy()
        for i in range(n-1):
            c[i+1] = cal(c[i], c[i+1], res[i])

        if max_ans < c[n-1]:
            max_ans = c[n-1]
        if min_ans > c[n-1]:
            min_ans = c[n-1]
        return

    for i1 in range(4):
        if arr[i1] > 0:
            arr[i1] -= 1
            res.append(dic[i1])
            dfs(res, a+1)
            res.pop()
            arr[i1] += 1

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    operator = []
    dic = {0: '+', 1: '-', 2: '*', 3: '/'}

    max_ans = -1e9
    min_ans = 1e9

    dfs([], 0)

    print(f'#{test_case}', max_ans - min_ans)