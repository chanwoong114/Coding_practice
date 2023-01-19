N = int(input())

L = []

for i in range(N//5+1):
    count = 0
    M = N - (5*i)
    count += i
    if M%3 == 0:
        L.append(count + M//3)
    
if L == []:
    print(-1)
else:
    print(min(L))