n = int(input())
count = 0
if n == 1:
    print(9)
else:
    m = 10**n
    k = m//10
    DP = [0]*m
    count = 0
    for i in range(k, m):
        for j in range(len(str(i))-1):
            if abs(int(str(i)[j])-int(str(i)[j+1])) == 1:
                count +=1
        if count == len(str(i))-1:
            DP[i] = 1
        DP[i] += DP[i-1]
    
    print(DP[n-1])