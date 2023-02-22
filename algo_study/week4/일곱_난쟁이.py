lst = [int(input()) for _ in range(9)]
visited = [0]*9
ans = []
def per(n, S, res):
    if len(ans):
        return
    if S > 100:
        return
    if n == 7:
        if S == 100:
            temp = [i for i in res]
            ans.append(temp)
            return

    for i in range(9):
        if not visited[i]:
            visited[i] = 1
            res.append(lst[i])
            per(n+1, S + lst[i], res)
            visited[i] = 0
            res.pop()

per(0, 0, [])

for i in sorted(ans[0]):
    print(i)