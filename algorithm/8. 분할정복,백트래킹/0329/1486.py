def combi(k, j, S):
    global minV
    if S >= m:
        minV = min(S-m, minV)
        return

    for i in range(j, n):
        combi(k+1, i+1, S+arr[i])

T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    minV = 1e9

    combi(0, 0, 0)
    print(f'#{test_case}', minV)