arr = [1,2,3,4,5]

for i in range(4, -1, -1): 
    for j in range(i):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)

# count = [0]*6
# for i in range(5):
#     count[arr[i]] += 1

# for i in range(6):
#     for j in range(count[i]):
#         print(i)

# def Counting_sort(DATA, COUNTS, k):
#     # DATA [] -- 입력 배열(0 to k)
#     # COUNTS [] -- 정렬된 배열.
#     # TEMP [] -- 카운트 배열.

#     TEMP = [0]*(k+1)

#     for i in range(len(DATA)):
#         TEMP[DATA[i]] += 1
    
#     for i in range(1, len(TEMP)):
#         TEMP[i] += TEMP[i-1]
    
#     for i in range(len(COUNTS)-1, -1, -1):
#         TEMP[DATA[i]] -= 1
#         COUNTS[TEMP[DATA[i]]] = DATA[i]
    
#     return COUNTS

# lst = [0, 4, 1, 3, 1, 2, 4, 1]
# sort_lst = [0] * len(lst)

# print(Counting_sort(lst, sort_lst, len(lst)))

# def merge_sort(arr):
#     if len(arr) < 2:
#         return arr

#     mid = len(arr) // 2
#     low_arr = merge_sort(arr[:mid])
#     high_arr = merge_sort(arr[mid:])

#     merged_arr = []
#     l = h = 0
#     while l < len(low_arr) and h < len(high_arr):
#         if low_arr[l] < high_arr[h]:
#             merged_arr.append(low_arr[l])
#             l += 1
#         else:
#             merged_arr.append(high_arr[h])
#             h += 1
#     merged_arr += low_arr[l:]
#     merged_arr += high_arr[h:]
#     return merged_arr

# print(merge_sort(arr))

# T = 1
# for test_case in range(1, T+1):
#     set_nums, set_sum = 3, 10
#     set_numbers = list(range(1, 13))
 
#     want_set = []
 
#     def nCr(n, ans, r):
#         if n == len(set_numbers):
#             if len(ans) == r:
#                 temp = [i for i in ans]
#                 want_set.append(temp)
#             return
#         ans.append(set_numbers[n])
#         nCr(n + 1, ans, r)
#         ans.pop()
#         nCr(n + 1, ans, r)
 
#     nCr(0, [], set_nums)
 
#     count = 0
 
#     for i in want_set:
#         sum_set = 0
#         for j in i:
#             sum_set += j
#         if sum_set == set_sum:
#             count += 1
 
#     print(f'#{test_case} {count}')

# def selectionSort(a, N):
#     for i in range(N-1):
#         minIdx = i
#         for j in range(i+1, N):
#             if a[minIdx] > a[j]:
#                 minIdx = j
#         a[i], a[minIdx] = a[minIdx], a[i]
#     return a

# print(selectionSort([7,5,8,6,4,5], 6))