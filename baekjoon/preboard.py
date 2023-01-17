N = int(input())
D = [0]*(N+1)
m = N

for i in range(2, N+1):
    if i%3==0:
        if i%2==0: #3, 2 둘 다 나뉘는 경우
            D[i] = min(D[i//3], D[i//2], D[i-1])+1
        else: # 3으로만 나뉘는 경우
            D[i] = min(D[i//3], D[i-1])+1
    elif i%2==0: # 2로만 나뉘는 경우
        D[i] = min(D[i//2], D[i-1])+1
    else: # 아무것도 나뉘지 않는 경우
        D[i] = D[i-1]+1

history=[]
history.append(N)

while N>3:
    if N%3==0:
        if N%2==0:
            if D[N//3] <= D[N//2]:
                if D[N//3] <= D[N-1]:
                    history.append(N//3)
                    N = N//3
                else:
                    history.append(N-1)
                    N = N-1
            else:
                if D[N//2] <= D[N-1]:
                    history.append(N//2)
                    N = N//2
                else:
                    history.append(N-1)
                    N = N-1
        else:
            if D[N//3] <= D[N-1]:
                history.append(N//3)
                N = N//3
            else:
                history.append(N-1)
                N = N-1

    elif N%2==0:
        if D[N//2] <= D[N-1]:
            history.append(N//2)
            N = N//2
        else:
            history.append(N-1)
            N = N-1
    else:
        history.append(N-1)
        N = N-1


print(D[m])
history.append(1)
print(*history)