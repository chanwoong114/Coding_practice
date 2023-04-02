def change(k, lst):
    global maxV
    if k == m or k == len(arr):
        s = ''.join(lst)
        if maxV < s:
            maxV = s
        return

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            lst[i], lst[j] = lst[j], lst[i]
            change(k+1, lst)
            lst[i], lst[j] = lst[j], lst[i]



T = int(input())
for test_case in range(1, T+1):
    n, m = map(str, input().split())
    m = int(m)
    arr = list(map(str, n.strip()))
    maxV = ''

    change(0, arr)
    print(f'#{test_case}', maxV)