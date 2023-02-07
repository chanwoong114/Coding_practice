n = int(input())
p = 1000000007

fib = [[1, 1],[1, 0]]

def multiply(a, b):
    z = [[0]*2 for _ in range(2)]

    for i in range(2):
        for j in range(2):
            v = 0
            for k in range(2):
                v += a[i][k] * b[k][j]
            z[i][j] = v%p
    return z

def square(A, k):
    if k == 1:
        for i in range(2):
            for j in range(2):
                A[i][j] %= p
        return A
    else:
        temp = square(A, k//2)
        if k%2:
            return multiply(multiply(temp, temp), A)
        else:
            return multiply(temp, temp)
        
print(square(fib, n)[0][1])


