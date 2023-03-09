n, m = map(int, input().split())
jack = list(map(int, input().split()))
ans = []
visited = [0] * n

def per(res):
    if sum(res) > m:
        return
    if len(res) == 3:
        ans.append(sum(res))
        return

    for i in range(len(jack)):
        if not visited[i]:
            visited[i] = 1
            res.append(jack[i])
            per(res)
            res.pop()
            visited[i] = 0

per([])

print(max(ans))