def fermat(a, b):
    if b == 0:
        return 1
    if b % 2:
        return (fermat(a, b//2) ** 2 * a) % p
    else:
        return (fermat(a, b //2) ** 2) % p
    
p = 1000000007
n, k = map(int, input().split())

factorial = [1 for _ in range(n+1)]

for i in range(2, n+1):
    factorial[i] = factorial[i-1] * i % p

A = factorial[n]
B = (factorial[n - k] * factorial[k]) % p

print((A % p) * (fermat(B, p - 2) % p) % p)