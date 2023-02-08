arr1 = [[9, 20, 2, 18, 11], [19, 1, 25, 3, 21], [8, 24, 10, 17, 7], [15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]
newarr = []
for i in arr1:
    for j in i:
        newarr.append(j)

def selectsort(arr, n):
    for i in range(0, n):
        minindex = i
        for j in range(i+1, n):
            if arr[minindex] > arr[j]:
                minindex = j
        arr[i], arr[minindex] = arr[minindex], arr[i]
    return arr

newarr = selectsort(newarr, 25)
n = len(arr1)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
direct = 0

snail = [[0]*n for _ in range(n)]

for i in newarr:
    snail[x][y] = i
    newx = x + dx[direct]
    newy = y + dy[direct]

    if newx < 0 or newx >= n or newy < 0 or newy >= n or snail[newx][newy]:
        direct = (direct + 1) % 4

    x = x + dx[direct]
    y = y + dy[direct]

for i in snail:
    print(*i)