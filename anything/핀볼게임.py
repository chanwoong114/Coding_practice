dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

turn = [(),
        (1, 0)]

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
