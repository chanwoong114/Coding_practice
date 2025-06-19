def per(k, d, res):
    if k == 6:
        print(*res)
        return

    for i in range(d, n):
        if not visited[i]:
            res.append(arr[i])
            visited[i] = 1
            per(k+1, i, res)
            visited[i] = 0
            res.pop()


while True:
    arr = list(map(int, input().split()))

    n = arr.pop(0)

    if n == 0:
        break

    arr.sort()

    visited = [0] * n
    per(0, 0, [])
    print()