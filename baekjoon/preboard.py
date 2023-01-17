# 1018 : 체스판 다시 칠하기

n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(input()))

def paint(L):
    LL = L.copy()
    count1, count2 = 0,0
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0:
                if LL[i][j] != 'W':
                    count1 += 1
            else:
                if LL[i][j] != 'B':
                    count1 += 1
    LL = L.copy()
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0:
                if LL[i][j] != 'B':
                    count2 += 1
            else:
                if LL[i][j] != 'W':
                    count2 += 1
    
    if count1<count2:
        return count1
    else:
        return count2


d = []
for k in range(n-7):
    for l in range(m-7):
        c = []
        for i in range(8):
            b = []
            for j in range(8):
                b.append(board[i+k][j+l])
            c.append(b)
        
        d.append(paint(c))

print(min(d))