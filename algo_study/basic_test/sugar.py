N = int(input())
L = []

for i in range(N//5+1):
    M = N - 5*i    
    if M%3==0:
        L.append(M//3+i)

if L:
    print(min(L))
else:
    print(-1)