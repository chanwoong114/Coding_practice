check = [0]*2 + [1]*9999

for i in range(10001):
    if check[i]:
        for j in range(i*2, 10001, i):
            check[j] = 0

m = int(input())
n = int(input())
sum_num = 0
min_num = 0

for i in range(n, m-1, -1):
    if check[i]:
        min_num = i
        sum_num += i

if min_num:
    print(sum_num)
    print(min_num)
else:
    print(-1)
