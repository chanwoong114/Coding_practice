n, m = map(int, input().split())
st = int(input())
lo = []

for _ in range(st):
    lo.append(list(map(int, input().split())))

dong = list(map(int, input().split()))

sumV = 0

if dong[0] == 1:
    for i in range(st):
        if lo[i][0] == 1:
            sumV += abs(dong[1] - lo[i][1])
        elif lo[i][0] == 2:
            sumV += min((dong[1] + m + lo[i][1]), (n - dong[1] + m + n - lo[i][1]))
        elif lo[i][0] == 3:
            sumV += dong[1] + lo[i][1]
        elif lo[i][0] == 4:
            sumV += (n - dong[1]) + lo[i][1]

elif dong[0] == 2:
    for i in range(st):
        if lo[i][0] == 1:
            sumV += min((dong[1] + m + lo[i][1]), (n - dong[1] + m + n - lo[i][1]))
        elif lo[i][0] == 2:
            sumV += abs(dong[1] - lo[i][1])
        elif lo[i][0] == 3:
            sumV += dong[1] + m - lo[i][1]
        elif lo[i][0] == 4:
            sumV += n - dong[1] + m - lo[i][1]

elif dong[0] == 3:
    for i in range(st):
        if lo[i][0] == 1:
            sumV += dong[1] + lo[i][1]
        elif lo[i][0] == 2:
            sumV += m - dong[1] + lo[i][1]
        elif lo[i][0] == 3:
            sumV += abs(dong[1] - lo[i][1])
        elif lo[i][0] == 4:
            sumV += min((dong[1] + n + lo[i][1]), (m - dong[1] + n + m - lo[i][1]))

elif dong[0] == 4:
    for i in range(st):
        if lo[i][0] == 1:
            sumV += dong[1] + n - lo[i][1]
        elif lo[i][0] == 2:
            sumV += m - dong[1] + n - lo[i][1]
        elif lo[i][0] == 3:
            sumV += min((dong[1] + n + lo[i][1]), (m - dong[1] + n + m - lo[i][1]))
        elif lo[i][0] == 4:
            sumV += abs(dong[1] - lo[i][1])

print(sumV)
