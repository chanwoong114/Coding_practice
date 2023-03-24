def rotation1(arr):
    arr.insert(0, arr.pop())
    return arr

def rotation2(arr):
    arr.append(arr.pop(0))
    return arr

def dfs(n, d):
    connect[n] = 0
    if d > 0:
        wheel[n] = rotation1(wheel[n])[:]
    else:
        wheel[n] = rotation2(wheel[n])[:]

    if n + 1 < 4 and connect[n + 1]:
        dfs(n + 1, -d)
    if n - 1 >= 0 and connect[n - 1]:
        dfs(n - 1, -d)

wheel = [list(map(int, input().strip())) for _ in range(4)]
t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    connect = [0, 0, 0]
    for j in range(3):
        if wheel[j][2] != wheel[j + 1][6]:
            connect[j] = 1
    connect.insert(x - 1, 0)
    dfs(x-1, y)

total = 0
for i in range(4):
    if wheel[i][0]:
        total += 2**i

print(total)