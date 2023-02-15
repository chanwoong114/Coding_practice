n = int(input())
lst = [list(map(int, input().split())) for _ in range(6)]

long_r, long_c, r, c = 0, 0, 0, 0
short_r, short_c = 0, 0

for i in range(6):
    if lst[i][0] == 1 or lst[i][0] == 2:
        if lst[i][1] > long_r:
            long_r = lst[i][1]
            r = i
    else:
        if lst[i][1] > long_c:
            long_c = lst[i][1]
            c = i

short_r = abs(lst[(r+1)%6][1] - lst[(r-1)%6][1])
short_c = abs(lst[(c+1)%6][1] - lst[(c-1)%6][1])

area = long_r * long_c - short_r * short_c

print(area*n)