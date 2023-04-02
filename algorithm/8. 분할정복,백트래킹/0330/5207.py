def binary_search(low, high, target, d):
    global cnt

    while True:
        mid = (low + high) // 2
        if target == arr1[mid]:
            cnt += 1
            break
        elif target < arr1[mid]:
            if d != 0:
                high = mid - 1
                d = 0
            else:
                break
        else:
            if d != 1:
                low = mid + 1
                d = 1
            else:
                break
    return


T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    cnt = 0
    arr1.sort()
    for i in range(m):
        if arr2[i] in arr1:
            binary_search(0, n-1, arr2[i], 2)

    print(f'#{test_case}', cnt)