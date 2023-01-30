# a, b, v = map(int, input().split())
a, b, v = map(int, input().split())

difference = a-b
day = 1
v -= a
if v%difference == 0:
    day += v//difference
else:
    day += v//difference + 1

print(day)