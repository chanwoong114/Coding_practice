def per(res):
    if len(res) == n//2:
        temp = [iii for iii in res]
        arr.append(temp)
        return

    for i1 in range(n):
        if not visited[i1]:
            if res and res[-1] > i1:
                continue
            visited[i1] = 1
            res.append(i1)
            per(res)
            res.pop()
            visited[i1] = 0

def cooking(arr1):
    res = []
    visit = [0] * (n//2)
    def per2(res1):
        if len(res1) == 2:
            temp = [iii for iii in res1]
            res.append(temp)
            return

        for i1 in range(n//2):
            if not visit[i1]:
                if res1 and res1[-1] > arr1[i1]:
                    continue
                visit[i1] = 1
                res1.append(arr1[i1])
                per2(res1)
                res1.pop()
                visit[i1] = 0
    per2([])
    sumV = 0

    for k in res:
        sumV += board[k[0]][k[1]] + board[k[1]][k[0]]

    return sumV

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    arr = []
    per([])
    cook =[]

    for i in arr:
        a = cooking(i)
        newA = []
        for j in range(n):
            if j not in i:
                newA.append(j)
        b = cooking(newA)
        cook.append(abs(a-b))


    print(f'#{test_case}', min(cook))
