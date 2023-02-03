a, b, c = map(int, input().split())

def multiply(a, b):
    if b == 1:
        return a%c
    else:
        res = multiply(a, b//2)
        if b%2:
            return res*res*a%c
        else:
            return res*res%c

print(multiply(a,b))