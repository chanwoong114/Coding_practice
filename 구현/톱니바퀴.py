def rotation_1(arr):
    save = arr[-1]
    for aa in range(7, 0, -1):
        arr[aa] = arr[aa - 1]
    arr[0] = save
    return arr


def rotation_2(arr):
    save = arr[0]
    for aa in range(7):
        arr[aa] = arr[aa + 1]
    arr[-1] = save
    return arr


def dfs(n, d):
    if d % 2:
        wheel[n] = rotation_1(wheel[n])[:]
    else:
        wheel[n] = rotation_2(wheel[n])[:]

    for bb in range(2):
        if bb % 2:
            if n - 1 < 0:
                continue
            elif not connect[n - 1]:
                continue
            else:
                connect[n - 1] = 0
                dfs(n - 1, d + 1)

        else:
            if n + 1 >= 4:
                continue
            elif not connect[n + 1]:
                continue
            else:
                connect[n + 1] = 0
                dfs(n + 1, d + 1)



wheel = [list(map(int, input().rstrip())) for _ in range(4)]
k = int(input())
order = [list(map(int, input().split())) for _ in range(k)]
connect = [0, 0, 0]

for i in order:
    connect = [0, 0, 0]
    cnt = 0
    for j in range(3):
        if wheel[j][2] != wheel[j + 1][6]:
            connect[j] = 1
    connect.insert(i[0] - 1, 0)
    if i[1] > 0:
        dfs(i[0] - 1, 1)
    else:
        dfs(i[0] - 1, 0)

ans = 0
for i in range(4):
    ans += wheel[i][0] * (2 ** i)
print(ans)