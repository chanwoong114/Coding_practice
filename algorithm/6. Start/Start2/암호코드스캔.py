import sys
sys.stdin = open("sample_input.txt", 'r')

d = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
     '4': '0100', '5': '0101', '6': '0110', '7': '0111',
     '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
     'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

pattern = {'211': 0, '221': 1, '122': 2,
           '411': 3, '132': 4, '231': 5,
           '114': 6, '312': 7, '213': 8,
           '112': 9}


def divide(p1, p2, p3):
    min_num = min(p1, p2, p3)
    p1 //= min_num
    p2 //= min_num
    p3 //= min_num
    return str(p1) + str(p2) + str(p3)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    bin_arr = [''] * N
    for i in range(N):
        for j in range(M):
            bin_arr[i] += d[arr[i][j]]

    res = []
    visited = []
    ans = 0
    for i in range(N):
        p1 = p2 = p3 = 0
        for j in range(M * 4 - 1, -1, -1):
            if p2 == 0 and p1 == 0 and bin_arr[i][j] == '1':
                p3 += 1
            elif p3 > 0 and p1 == 0 and bin_arr[i][j] == '0':
                p2 += 1
            elif p3 > 0 and p2 > 0 and bin_arr[i][j] == '1':
                p1 += 1

            if p1 > 0 and p2 > 0 and p3 > 0 and bin_arr[i][j] == '0':
                res.append(pattern[divide(p1, p2, p3)])
                p1 = p2 = p3 = 0

            if len(res) == 8:
                res = res[::-1]
                sumV = 0
                for k in range(8):
                    if k % 2:
                        sumV += res[k]
                    else:
                        sumV += res[k] * 3

                if sumV % 10 == 0 and res not in visited:
                    ans += sum(res)

                visited.append(res)
                res = []

    print(f'#{tc}', ans)