def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        global cnt
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] <= arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1
        if l < mid and h == high:
            cnt += 1

        while l < mid:
            temp.append(arr[l])
            l += 1

        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    merge_sort(arr)
    print(f'#{test_case}', arr[n//2])