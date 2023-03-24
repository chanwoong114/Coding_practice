def dfs(a, b, n, s):
    if n == 5:
        if s not in visited:
            visited.append(s)
        return

    for k in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        na = a + k[0]
        nb = b + k[1]

        if 0 <= na < 5 and 0 <= nb < 5:
            ss = s + str(board[na][nb])
            dfs(na, nb, n+1, ss)


def dfs2(x, y):
    stack = [(x, y, str(board[i][j]))]

    while stack:
        a, b, s = stack.pop(0)
        if len(s) == 6:
            if s not in visited:
                visited.append(s)
            continue

        for k in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            na = a + k[0]
            nb = b + k[1]
            if 0 <= na < 5 and 0 <= nb < 5:
                ss = s + str(board[na][nb])
                stack.append((na, nb, ss))


board = [list(map(int, input().split())) for _ in range(5)]
visited = []

for i in range(5):
    for j in range(5):
        dfs2(i, j)

print(len(visited))