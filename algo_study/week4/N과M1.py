def per(a, res):
    if len(res) == m:
        print(*res)
        return

    for i in range(n):
        if not visited[i]:
            res.append(lst[i])
            visited[i] = 1
            per(a+1, res)
            res.pop()
            visited[i] = 0


n, m = map(int, input().split())
lst = list(range(1, n+1))
visited = [0]*n
ans = []

per(0, [])

for i in ans:
    print(*i)

