import sys
input = sys.stdin.readline

def combi(n, ans, r):
    if n == len(nums):
        if len(ans) == r:
            temp = [i for i in ans]
            answer.append(temp)
        return
    ans.append(nums[n])
    combi(n+1, ans, r)
    ans.pop()
    combi(n+1, ans, r)

n, m = map(int, input().split())
answer = []
lst = [list(map(int, input().split())) for _ in range(n)]
home, chicken, result = [], [], []

for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:
            home.append((i,j))
        elif lst[i][j] == 2:
            chicken.append((i,j))

nums = list(range(len(chicken)))
combi(0,[],m)

for i in answer:
    res = 0
    for k in range(len(home)):
        distance = 1e9
        for j in i:
            distance = min(distance, abs(chicken[j][0]-home[k][0])+abs(chicken[j][1]-home[k][1]))
        res += distance
    result.append(res)

print(min(result))