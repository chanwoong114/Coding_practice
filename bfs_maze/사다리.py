for _ in range(10):
    t = int(input())

    map_matrix = [list(map(int,input().split())) for _ in range(100)]

    start_list = []
    for i in range(100):
        if map_matrix[0][i] == 1:
            start_list.append([0, i])

    drow = [0, 0, 1]
    dcol = [-1, 1, 0]

    for s in start_list:
        flag = 0
        [start_row, start_col] = s
        check_map = [[0] * 100 for _ in range(100)]
        while 1:

            for i in range(3):
                trow = start_row + drow[i]
                tcol = start_col + dcol[i]

                if trow >= 0 and trow <= 99 and tcol >= 0 and tcol <= 99 :
                    if trow == 99 and map_matrix[trow][tcol] == 2 and check_map[trow][tcol] == 0:
                        flag = 1
                        result = s[1]
                        break
                    elif trow == 99 and check_map[trow][tcol] == 0 and map_matrix[trow][tcol] == 1:
                        flag = 2
                        break
                    elif map_matrix[trow][tcol] == 1 and check_map[trow][tcol] == 0:
                        start_row = trow
                        start_col = tcol
                        check_map[trow][tcol] = 1

            if flag == 1:
                break
            elif flag == 2:
                break
        if flag == 1:
            break

    print(f'#{t} {result}')