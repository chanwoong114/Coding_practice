from itertools import combinations
from collections import deque

def dfs(people, stair):
    s = []
    # 계단까지 가는 시간
    for person in people:
        s.append(abs(person[0] - stair[0]) + abs(person[1] - stair[1]))

    # 계단을 내려가서 도착하는 시간
    s = deque(sorted(s))
    e = deque()

    t = 0
    c = 0

    while s:
        t += 1
        while e and e[0] == t:
            e.popleft()
            c -= 1

        while s[0] < t:
            if c < 3:
                s.popleft()
                if not s:
                    t += board[stair[0]][stair[1]]
                    break

                e.append(t + board[stair[0]][stair[1]])
                c += 1
            else:
                break

    return t


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stair = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                people.append((i, j))
            elif board[i][j] > 1:
                stair.append((i, j))

    total = 1e9
    for n in range(N):
        for people1 in combinations(people, n):
            people2 = list(set(people) - set(people1))
            t = max(dfs(people1, stair[0]), dfs(people2, stair[1]))
            total = min(total, t)

    print(f'#{test_case}', total)