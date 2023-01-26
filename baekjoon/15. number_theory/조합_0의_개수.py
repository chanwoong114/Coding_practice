N, K = map(int, input().split())

def two(n):
    count = 0
    while n != 0:
        n = n//2
        count += n

    return count

def five(n):
    count = 0
    while n != 0:
        n = n//5
        count += n

    return count

result = min(two(N) - two(N-K) - two(K), five(N) - five(N-K) - five(K))

print(result)