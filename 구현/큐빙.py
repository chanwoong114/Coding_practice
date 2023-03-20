def plus(d):
    dice[d][0][0], dice[d][0][2], dice[d][2][2], dice[d][2][0] = dice[d][2][0], dice[d][0][0], dice[d][0][2], \
        dice[d][2][2]
    dice[d][0][1], dice[d][1][2], dice[d][2][1], dice[d][1][0] = dice[d][1][0], dice[d][0][1], dice[d][1][2], \
        dice[d][2][1]


def minus(d):
    dice[d][2][0], dice[d][0][0], dice[d][0][2], dice[d][2][2] = dice[d][0][0], dice[d][0][2], dice[d][2][2], \
        dice[d][2][0]
    dice[d][1][0], dice[d][0][1], dice[d][1][2], dice[d][2][1] = dice[d][0][1], dice[d][1][2], dice[d][2][1], \
        dice[d][1][0]


def turn(i, j):
    if i == 'U':
        if j == '+':
            plus(0)
            for t in range(3):
                dice[5][t][0], dice[2][0][2 - t], dice[4][2 - t][2], dice[3][2][t] = dice[3][2][t], dice[5][t][0], \
                    dice[2][0][2 - t], dice[4][2 - t][2]
        if j == '-':
            minus(0)
            for t in range(3):
                dice[3][2][t], dice[5][t][0], dice[2][0][2 - t], dice[4][2 - t][2] = dice[5][t][0], dice[2][0][2 - t], \
                    dice[4][2 - t][2], dice[3][2][t]

    if i == 'D':
        if j == '+':
            plus(1)
            for t in range(3):
                dice[4][2 - t][0], dice[2][2][2 - t], dice[5][t][2], dice[3][0][t] = dice[3][0][t], dice[4][2 - t][0], \
                    dice[2][2][2 - t], dice[5][t][2]
        if j == '-':
            minus(1)
            for t in range(3):
                dice[3][0][t], dice[4][2 - t][0], dice[2][2][2 - t], dice[5][t][2] = dice[4][2 - t][0], dice[2][2][2 - t], \
                    dice[5][t][2], dice[3][0][t]

    if i == 'F':
        if j == '+':
            plus(2)
            for t in range(3):
                dice[5][2][t], dice[0][2][t], dice[4][2][t], dice[1][0][2 - t] = dice[0][2][t], dice[4][2][t], \
                    dice[1][0][2 - t], dice[5][2][t]
        if j == '-':
            minus(2)
            for t in range(3):
                dice[0][2][t], dice[4][2][t], dice[1][0][2 - t], dice[5][2][t] = dice[5][2][t], dice[0][2][t], \
                    dice[4][2][t], dice[1][0][2 - t]

    if i == 'B':
        if j == '+':
            plus(3)
            for t in range(3):
                dice[0][0][t], dice[5][0][t], dice[1][2][2 - t], dice[4][0][t] = dice[5][0][t], dice[1][2][2 - t], \
                    dice[4][0][t], dice[0][0][t]
        if j == '-':
            minus(3)
            for t in range(3):
                dice[5][0][t], dice[1][2][2 - t], dice[4][0][t], dice[0][0][t] = dice[0][0][t], dice[5][0][t], \
                    dice[1][2][2 - t], dice[4][0][t]

    if i == 'L':
        if j == '+':
            plus(4)
            for t in range(3):
                dice[0][t][0], dice[2][t][0], dice[1][t][0], dice[3][t][0] = dice[3][t][0], dice[0][t][0], \
                    dice[2][t][0], dice[1][t][0]
        if j == '-':
            minus(4)
            for t in range(3):
                dice[3][t][0], dice[0][t][0], dice[2][t][0], dice[1][t][0] = dice[0][t][0], dice[2][t][0], \
                    dice[1][t][0], dice[3][t][0]

    if i == 'R':
        if j == '+':
            plus(5)
            for t in range(3):
                dice[0][t][2], dice[2][t][2], dice[1][t][2], dice[3][t][2] = dice[2][t][2], dice[1][t][2], \
                    dice[3][t][2], dice[0][t][2]
        if j == '-':
            minus(5)
            for t in range(3):
                dice[2][t][2], dice[1][t][2], dice[3][t][2], dice[0][t][2] = dice[0][t][2], dice[2][t][2], \
                    dice[1][t][2], dice[3][t][2]


T = int(input())
for _ in range(T):
    dice = [[['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']],
            [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],
            [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
            [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],
            [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
            [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]
            ]
    n = int(input())
    order = list(map(str, input().split()))
    for o in order:
        turn(o[0], o[1])

    for k in dice[0]:
        print("".join(k))
