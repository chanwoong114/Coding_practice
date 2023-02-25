
def solution(boards):
    answer = []
    def check():
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    return 0
        return 1

    def dfs(r, c):
        k = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        d = 0
        while True:
            nr = r + k[d]
            nc = c + k[d]






    for tc in boards:
        board = []
        for j in tc:
            board.append(list(map(int, j.strip())))

        n = len(board[0])
        visited = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if board[i][j] == 2:
                    x, y = i, j


    return answer



print(solution([["00011", "01111", "21001", "11001", "01111"], ["00011", "00011", "11111", "12101", "11111"]]))
print(solution([["1111", "1121", "1001", "1111"], ["0000", "0000", "0000", "0002"], ["0000", "0100", "0000", "0002"], ["0000", "0010", "0121", "0010"]]))