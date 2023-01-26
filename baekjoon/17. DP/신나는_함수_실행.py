lst = [[[0 for _ in range(51)] for _ in range(51)] for _ in range(51)]

for i in range(51):
    for j in range(51):
        for k in range(51):
            if i <= 0 or j <= 0 or k <= 0:
                lst[i][j][k] = 1
            elif i > 20 or j > 20 or k > 20:
                lst[i][j][k] = 1048576
            elif i < j and j < k:
                lst[i][j][k] = lst[i][j][k-1] + lst[i][j-1][k-1] - lst[i][j-1][k]
            else:
                lst[i][j][k] = lst[i-1][j][k] + lst[i-1][j-1][k] + lst[i-1][j][k-1] - lst[i-1][j-1][k-1]


while True:
    a,b,c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    if a<0 or b<0 or c<0:
        print(f'w({a}, {b}, {c}) = {1}')
    else:
        print(f'w({a}, {b}, {c}) = {lst[a][b][c]}')

    



# def w(a,b,c):

#     if a <= 0 or b <= 0 or c <= 0:
#         return 1
#     if a > 20 or b > 20 or c > 20:
#         return w(20,20,20)
#     if a < b and b < c:
#         return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
#     else:
#         return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    
# print(w(1, 1, 49))

import sys
input = sys.stdin.readline

def w(a, b, c):
    if a <= 0 or b<= 0 or c<=0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp[a][b][c]:
        return dp[a][b][c]
    if a<b<c:
        dp[a][b][c] = w(a,b,c-1)+w(a,b-1,c-1)-w(a, b-1, c)
        return dp[a][b][c]
    dp[a][b][c] = w(a-1, b, c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
    return dp[a][b][c]

dp = [[[0]*(21) for _ in range(21)] for _ in range(21)]
# 0~20까지므로

while 1:
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')