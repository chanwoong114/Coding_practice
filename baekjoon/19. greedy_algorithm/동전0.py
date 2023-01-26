N, K = map(int, input().split())

won = [int(input()) for _ in range(N)]
count = 0

for i in range(N-1, -1, -1):
    if K//won[i]:
        count += K//won[i]
        K = K%won[i]
    if K==0:
        break    

print(count)