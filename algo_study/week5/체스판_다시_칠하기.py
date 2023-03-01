def paint(arr):
    count1, count2 = 0, 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2:
                if arr[i][j] != 'W':
                    count1 += 1
            else:
                if arr[i][j] != 'B':
                    count1 += 1

    for i in range(8):
        for j in range(8):
            if (i + j) % 2:
                if arr[i][j] != 'B':
                    count2 += 1
            else:
                if arr[i][j] != 'W':
                    count2 += 1

    if count1 > count2:
        return count2
    else:
        return count1

n, m = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(n)]

a = []
for k in range(n-7):
    for l in range(m-7):
        c = []
        for kk in range(8):
            d = []
            for ll in range(8):
                d.append(board[k+kk][l+ll])
            c.append(d)
        a.append(paint(c))

print(min(a))