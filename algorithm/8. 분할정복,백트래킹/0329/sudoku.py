def small_sdoku(v, w):
    ss = []
    for i in range(v, v + 3):
        ss += sdoku[i][w:w + 3]

    if ss.count(0) == 1:
        num = 45 - sum(ss)
        idx = ss.index(0)
        ss[idx] = num

        sdoku[v][w:w + 3] = ss[0:3]
        sdoku[v + 1][w:w + 3] = ss[3:6]
        sdoku[v + 2][w:w + 3] = ss[6:]
        return

    else:
        return


sdoku = [list(map(int, input().split())) for _ in range(9)]

while True:
    sumV = 0
    for p in range(9):  # sdoku에 0이 몇개있는지 계산
        sumV += sdoku[p].count(0)

    if sumV == 0:  # sdoku에 0이 없으면 끝
        break

    for i in range(9):  # 행으로 봤을 때 0이 하나 있는 자리에 숫자 채우기
        if sdoku[i].count(0) == 1:
            num = 45 - sum(sdoku[i])
            idx = sdoku[i].index(0)
            sdoku[i][idx] = num
        else:
            continue

    for a in range(9):  # 열로 봤을 때 0이 하나 있는 자리에 숫자 채우기
        col_sdoku = []
        for b in range(9):
            col_sdoku.append(sdoku[b][a])

        if col_sdoku.count(0) == 1:
            num = 45 - sum(col_sdoku)
            idx = col_sdoku.index(0)
            col_sdoku[idx] = num

            for m in range(9):
                sdoku[m][a] = col_sdoku[m]
        else:
            continue

    for v in range(0, 9, 3):
        for w in range(0, 9, 3):
            small_sdoku(v, w)

for k in range(9):
    print(*sdoku[k])