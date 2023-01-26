def fib_dp(n):
    f = [0]*n
    f[0], f[1] = 1, 1
    for i in range(2, n):
        f[i] = f[i-1] + f[i-2]

    return f[n-1], len(f)-2

def fib_recursion(n):
    if n==1 or n==2:
        return 1
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)



N = int(input())


print(fib_dp(N)[0], fib_dp(N)[1])