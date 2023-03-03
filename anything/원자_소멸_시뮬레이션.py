import sys
sys.stdin = open("sample_input.txt", "r")

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    queue = []

    for _ in range(n):
        x, y, d, v = map(int, input().split())
        queue.append([x * 2 + 2000, y * 2 + 2000, d, v])

    e = 0
    while len(queue) >= 2:
        dic = {}
        for x, y, d, v in queue:
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx > 4000 or ny < 0 or ny > 4000:
                continue

            dic[(nx, ny)] = dic.get((nx, ny), [])
            dic[(nx, ny)].append([d, v])
        queue = []

        for a, b in dic.items():
            if len(dic[a]) > 1:
                for i in b:
                    e += i[1]

            else:
                queue.append([a[0], a[1], b[0][0], b[0][1]])

    print(f'#{test_case}', e)
