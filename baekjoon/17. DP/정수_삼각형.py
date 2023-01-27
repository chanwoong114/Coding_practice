N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

for i in range(N-1, 0, -1):
    for j in range(i):
        lst[i-1][j] += max(lst[i][j], lst[i][j+1])

print(lst[0][0])