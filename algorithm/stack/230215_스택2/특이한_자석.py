def rotation_1(arr):
    save = arr[-1]
    for aa in range(7, 0, -1):
        arr[aa] = arr[aa-1]
    arr[0] = save
    return arr

def rotation_2(arr):
    save = arr[0]
    for aa in range(7):
        arr[aa] = arr[aa+1]
    arr[-1] = save
    return arr

def dfs(n, d):
    if d%2:
        wheel[n] = rotation_1(wheel[n])[:]
    else:
        wheel[n] = rotation_2(wheel[n])[:]

    for bb in range(2):
        if bb%2:
            if n-1<0:
                break
            elif not connect[n-1]:
                break
            else:
                connect[n-1] = 0
                dfs(n-1, d+1)

        else:
            if n+1>=4:
                break
            elif not connect[n+1]:
                break
            else:
                connect[n+1] = 0
                dfs(n+1, d+1)


T = int(input())
for test_case in range(1, T+1):
    k = int(input())
    wheel = [list(map(int, input().split())) for _ in range(4)]

    order = [list(map(int, input().split())) for _ in range(k)]

    connect = [0,0,0]

    for i in order:
        connect = [0, 0, 0]
        cnt = 0
        for j in range(3):
            if wheel[j][2] != wheel[j+1][6]:
                connect[j] = 1
        connect.insert(i[0]-1, 0)

        if i[1] > 0:
            dfs(i[0]-1, 1)
        else:
            dfs(i[0]-1, 0)
        for k in wheel:
            print(*k)
        print(connect)


    ans = 0
    for i in range(4):
        ans += wheel[i][0]*((i+1)*2)
    print(ans)

