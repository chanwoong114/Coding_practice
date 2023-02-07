import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

start = 1
end = max(arr)

while start <= end:
    mid = (start+end)//2
    count = 0
    for i in arr:
        count += i//mid
    
    if count >= k:
        start = mid+1
    else:
        end = mid-1

print(end)