dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]

T = int(input())
for test_case in range(1, T + 1):
    m, a = map(int, input().split())
    m_a = list(map(int, input().split()))
    m_b = list(map(int, input().split()))
    ap = [list(map(int, input().split())) for _ in range(a)]
    ap.sort(key=lambda x: -x[3])
    a_start = [1, 1]
    b_start = [10, 10]
    total = 0

    for time in range(m + 1):
        al = []
        bl = []
        for idx in range(len(ap)):
            if abs(ap[idx][0] - a_start[0]) + abs(ap[idx][1] - a_start[1]) <= ap[idx][2]:
                al.append(idx)
            if abs(ap[idx][0] - b_start[0]) + abs(ap[idx][1] - b_start[1]) <= ap[idx][2]:
                bl.append(idx)
        curmax = 0
        if al or bl:
            if al and bl:
                if al[0] == bl[0]:
                    if len(al) > 1:
                        curmax = max(curmax, ap[al[1]][3] + ap[bl[0]][3])
                    if len(bl) > 1:
                        curmax = max(curmax, ap[bl[1]][3] + ap[al[0]][3])
                else:
                    curmax = max(curmax, ap[al[0]][3] + ap[bl[0]][3])

            if al:
                curmax = max(curmax, ap[al[0]][3])
            if bl:
                curmax = max(curmax, ap[bl[0]][3])
        total += curmax
        if time == m:
            continue
        a_start[0] += dx[m_a[time]]
        a_start[1] += dy[m_a[time]]
        b_start[0] += dx[m_b[time]]
        b_start[1] += dy[m_b[time]]


    print(f'#{test_case}', total)
