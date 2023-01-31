check = [0]*2 + [1]*999999

for i in range(2, 1000001):
    if check[i]:
        for j in range(i*2, 1000001, i):
            check[j] = 0

a,b = map(int, input().split())

for i in range(a, b+1):
    if check[i]:
        print(i)