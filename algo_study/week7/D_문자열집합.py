n, m = map(int, input().split())
S = [str(input()) for _ in range(n)]
check = [str(input()) for _ in range(m)]

dic = {}
for i in S:
    dic[i] = 1

cnt = 0
for i in check:
    if i in dic:
        cnt += 1

print(cnt)