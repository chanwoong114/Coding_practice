n = int(input())
m = n
for i in range(2, n+1):
    while m%i == 0:
        print(i)
        m = m//i
    if m <= 1:
        break
