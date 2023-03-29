def quick_sort(arr):
    def sort(low, high):
        if low >= high:
            return

        mid = partition(low, high)
        sort(low, mid-1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high)]

        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr)-1)


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr)
    print(f'#{test_case}', arr[n // 2])