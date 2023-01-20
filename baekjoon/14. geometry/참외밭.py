# 2477 : 참외밭

N = int(input())

a = [list(map(int, input().split())) for _ in range(6)]

w, h, wnum, hnum = 0, 0, 0, 0

for i in range(6):
    if a[i][0] == 1 or a[i][0] == 2:
        if w < a[i][1]:
            w = a[i][1]
            wnum = i
    else:
        if h < a[i][1]:
            h = a[i][1]
            hnum = i

short_w, short_h = 0, 0

short_w = abs(a[(wnum-1)%6][1] - a[(wnum+1)%6][1])
short_h = abs(a[(hnum-1)%6][1] - a[(hnum+1)%6][1])

melon = (w*h - short_w*short_h) * N

print(melon)