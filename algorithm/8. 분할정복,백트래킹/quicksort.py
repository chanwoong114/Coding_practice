# def hoare(l, r):
#     p = l   # 피봇 위치 왼쪽 끝
#     lp = l+1
#     rp = r
#
#     while lp<=rp:
#         while lp<=rp and lst[lp] <= lst[p]:
#             lp += 1
#         while lp<=rp and lst[rp] >= lst[p]:
#             rp -= 1
#         if lp<rp:
#             lst[lp], lst[rp] = lst[rp], lst[lp]
#     lst[p], lst[rp] = lst[rp], lst[p]
#
#     return rp
#
# def lomuto(l, r):
#     p = r
#     i = l-1      # 경계지점
#     for j in range(l, r):
#         if lst[j] < lst[p]:
#             i += 1
#             lst[i], lst[j] = lst[j], lst[i]
#     i += 1
#     lst[i], lst[p] = lst[p], lst[i]
#
#     return i
#
#
# def quickS(l, r):
#     if l<r:
#         # p = hoare(l, r)
#         p = lomuto(l, r)
#         quickS(l, p-1)
#         quickS(p+1, r)
#
#
#
# lst = [3, 2, 4, 6, 9, 1, 8, 7, 5]
# quickS(0, 8)
# print(lst)

def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))
def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)