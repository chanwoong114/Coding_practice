import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

start = 1
end = max(arr)

while start<=end:
    mid = (start+end)//2
    tree = 0
    for i in arr:
        if i > mid:
            tree += i-mid
    
    if tree >= k:
        start = mid+1
    else:
        end = mid-1
        

print(end)