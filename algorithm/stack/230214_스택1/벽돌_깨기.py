from copy import deepcopy

def permutation(result):
    if len(result) == n:
        temp = [i for i in result]
        lst.append(temp)
        return
    for i in range(w):
        result.append(arr[i])
        permutation(result)
        result.pop()

T = int(input())
for test_case in range(1, T+1):
    n, w, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]
    board2 = deepcopy(board)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    result = [0] * n  # 출력 배열
    arr = list(range(w))
    lst = []

    permutation([])

    def block(a):
        for aaa in range(h):
            if board2[aaa][a]:
                return aaa
        return -1

    def break_block(x, y, k):
        board2[x][y] = 0
        if k > 1:
            for a in range(4):
                for b in range(1, k):
                    nx = x + dx[a]*b
                    ny = y + dy[a]*b

                    if 0 <= nx < h and 0 <= ny < w and board2[nx][ny]:
                        break_block(nx, ny, board2[nx][ny])

    def clear(board2):
        global arr
        for i in range(w):
            arr = [0] * h
            idx = h-1
            for j in range(h-1, -1, -1):
                if board2[j][i]:
                    arr[idx] = board2[j][i]
                    idx -= 1
            for j in range(h):
                board2[j][i] = arr[j]


    min_total = 1e9
    for i in [[5,5,5]]:
        cnt = 0
        board2 = deepcopy(board)
        for j in i:
            if block(j)>=0:
                x, y = block(j), j
                break_block(x, y, board2[x][y])
                clear(board2)
        for j in range(h):
            for l in range(w):
                if board2[j][l]:
                    cnt += 1
        if min_total > cnt:
            min_total = cnt

    print(f'#{test_case}', min_total)
