bingo_board = [list(map(int, input().split())) for _ in range(5)]

checkNum = [list(map(int, input().split())) for _ in range(5)]

checklst = []
for i in checkNum:
    checklst += i

visited = [[0] * 5 for _ in range(5)]



ans = 0
for k in range(0, 25):
    for i in range(5):
        for j in range(5):
            if checklst[k] == bingo_board[i][j]:
                visited[i][j] = 1
                c = 0
                v2 = 0
                v4 = 0
                for a in range(5):
                    v1 = 0
                    v3 = 0

                    for b in range(5):
                        v1 += visited[a][b]
                        v3 += visited[b][a]
                    if v1 == 5:
                        c += 1
                    if v3 == 5:
                        c += 1

                    v2 += visited[a][a]
                    v4 += visited[a][4 - a]

                if v2 == 5:
                    c += 1
                if v4 == 5:
                    c += 1

                if c >= 3:
                    print(k+1)
                    exit(0)

