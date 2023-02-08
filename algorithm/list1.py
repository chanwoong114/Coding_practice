def selectsort(arr, n):
    for i in range(0, n):
        minindex = i
        for j in range(i+1, n):
            if arr[minindex] > arr[j]:
                minindex = j
        arr[i], arr[minindex] = arr[minindex], arr[i]
    return arr

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = selectsort(arr, n)
    lst = []

    if n%2:
        for i in range(5):
            lst.append(arr[n-1-i])
            lst.append(arr[i])
    else:
        for i in range(5):
            lst.append(arr[n-1-i])
            lst.append(arr[i])


    print(f'#{test_case}', *lst)