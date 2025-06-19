def per(k, res):
    if k == n:
        print(*res)
        return

    for i in range(1, n+1):
        if not visited[i]:
            res.append(i)
            visited[i] = 1
            per(k+1, res)
            visited[i] = 0
            res.pop()


n = int(input())
visited = [0] * (n+1)

per(0, [])