def solution(n, m, k):
    arr = list(range(1, k+1))
    answer = 0
    ans = []
    def per(res):
        if sum(res) > m:
            return

        if len(res) == n:
            if sum(res) == m:
                temp = [i for i in res]
                ans.append(temp)
            return

        for i in range(k):
            res.append(arr[i])
            per(res)
            res.pop()

    per([])

    return len(ans)

print(solution(3, 6, 3))
print(solution(10, 6, 5))