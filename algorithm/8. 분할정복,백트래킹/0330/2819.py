def dfs(a, b, res):
    if len(res) == 7:
        if res not in visited:
            print(res)
            temp = [i for i in res]
            visited.append(temp)
        return

    for i in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        na = a + i[0]
        nb = b + i[1]

        if 0 <= na < 4 and 0 <= nb < 4:
            res.append(board[na][nb])
            dfs(na, nb, res)
            res.pop()

T = int(input())
for test_case in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(4)]
    visited = []

    for i in range(4):
        for j in range(4):
            dfs(i, j, [board[i][j]])

    print(len(visited))
    print(visited)