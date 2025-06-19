def combi(k, sumV):
    global cnt

    if k == n:
        return

    sumV += arr[k]

    if sumV == s:
        cnt += 1

    combi(k + 1, sumV)
    combi(k + 1, sumV - arr[k])


n, s = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * n
cnt = 0
combi(0, 0)
print(cnt)