n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr.sort()
left, right = 0, n-1
cnt = 0

while left < right:
    temp = arr[left] + arr[right]
    if temp == m:
        cnt += 1
    elif temp < m:
        left += 1
    else:
        right += 1

print(cnt)
