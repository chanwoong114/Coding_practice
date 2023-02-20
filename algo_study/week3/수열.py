n, m = map(int, input().split())
arr = list(map(int, input().split()))

v = sum(arr[:m])
max_sum = v
for i in range(1, n-m+1):
    v = v - arr[i-1] + arr[i+m-1]
    max_sum = max(max_sum, v)

print(max_sum)