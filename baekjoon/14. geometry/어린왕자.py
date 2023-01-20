# 원과 점의 거리가 반지름보다 작다면 통과한다
# 원과 점의 거리가 반지름보다 크다면 통과하지않는다.

T = int(input())

for i in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    count = 0
    for j in range(N):
        c1, c2, r = map(int, input().split())
        
        if ((c1-x1)**2 + (c2-y1)**2)**.5 < r or ((c1-x2)**2 + (c2-y2)**2)**.5 < r:
            count += 1
            if  ((c1-x1)**2 + (c2-y1)**2)**.5 < r and ((c1-x2)**2 + (c2-y2)**2)**.5 < r:
                count -= 1

    print(count)