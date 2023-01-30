n, k = map(int, input().split())
lst = list(map(int, input().split()))
value = sum(lst[:k])
high = value
for i in range(n-k):
    value = value + lst[i+k] - lst[i]
    if high < value:
        high = value


print(high)
