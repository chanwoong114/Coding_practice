board = [[1, 1, 0, 0, 0], [1, 0, 1, 0, 2], [1, 1, 1, 1, 2], [0, 1, 1, 1, 4], [0, 0, 0, 0, 0]]
a = 5
for i in range(a):
    cnt = 0
    for j in range(a):
        if board[j][i]:
            for jj in range(j - 1, -1 + cnt, -1):
                if board[j][i] == board[jj][i]:
                    board[j][i] = 0
                    board[jj][i] *= 2
                    cnt += 1
                    break

                elif board[jj][i] and board[j][i] != board[jj][i]:
                    cnt += 1
                    save = board[j][i]
                    board[j][i] = 0
                    board[jj + 1][i] = save
                    break

                elif jj == cnt:
                    save = board[j][i]
                    board[j][i] = 0
                    board[jj][i] = save


print(board)