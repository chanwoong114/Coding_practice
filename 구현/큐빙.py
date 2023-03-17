def plus(d):
    dice[d] = list(zip(*dice[d][::-1]))

def minus(d):
    for _ in range(3):
        dice[d] = list(zip(*dice[d][::-1]))

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
    order = list(map(int, input().split()))

