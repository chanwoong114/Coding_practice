n = int(input())
arr = list(map(int, input().split()))

d = 0
cnt = 1
for i in range(n-1, 0, -1):
    if arr[i] >= arr[i-1]:
        cnt += 1
    else:
        if d < cnt:
            d = cnt
        cnt = 1

if d < cnt:
    d = cnt

cnt = 1
for i in range(n-1):
    if arr[i] >= arr[i+1]:
        cnt += 1
    else:
        if d < cnt:
            d = cnt
        cnt = 1

if d < cnt:
    d = cnt

print(d)