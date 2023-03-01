def distance(x, y):
    if x == 1:
        return y
    if x == 2:
        return r + c + r - y
    if x == 3:
        return 2*r + c + c - y
    if x == 4:
        return r + y

r, c = map(int, input().split())
n = int(input())
store = []
for _ in range(n):
    a, b = map(int, input().split())
    store.append(distance(a, b))

a, b = map(int, input().split())
start = distance(a, b)

sumV = 0
for i in range(n):
    diff = abs(start - store[i])
    sumV += min(diff, (2 * (r+c) - diff))

print(sumV)