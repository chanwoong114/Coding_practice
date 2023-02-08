lst = [[0]*101 for _ in range(101)]

for i in range(4):
    a,b,c,d = map(int, input().split())
    
    for i in range(a, c+1):
        for j in range(b, d+1):
            lst[i][j] = 1

print(sum(lst))