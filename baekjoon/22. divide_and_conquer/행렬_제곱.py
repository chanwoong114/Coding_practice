n, m = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(n)]


def multiply(B, C):
    lst = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            v = 0
            for k in range(n):
                v += B[i][k]*C[k][j]
            lst[i][j] = v%1000
    return lst

def square(A, m):
    if m == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A
    else:
        res = square(A, m//2)
        if m%2:
            return multiply(multiply(res, res), A)
        else:
            return multiply(res, res)

res = square(A, m)

for i in res:
    print(*i)