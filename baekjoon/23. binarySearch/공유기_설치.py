# 재귀 형태로 풀기?
# 포문 돌기?
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
home = [int(input()) for _ in range(n)]
home.sort()

start  = 1
end = home[n-1] - home[0]
res = 0

while start<=end:
    mid = (start+end)//2
    current = home[0]
    count = 1

    for i in range(1, n):
        if home[i] >= current + mid:
            count += 1
            current = home[i]
    
    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)