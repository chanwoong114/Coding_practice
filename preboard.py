arr = [1,2,3,4,5]

for i in range(4, -1, -1): 
    for j in range(i):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)

count = [0]*6
for i in range(5):
    count[arr[i]] += 1

for i in range(6):
    for j in range(count[i]):
        print(i)

def Counting_sort(DATA, COUNTS, k):
    # DATA [] -- 입력 배열(0 to k)
    # COUNTS [] -- 정렬된 배열.
    # TEMP [] -- 카운트 배열.

    TEMP = [0]*(k+1)

    for i in range(len(DATA)):
        TEMP[DATA[i]] += 1
    
    for i in range(1, len(TEMP)):
        TEMP[i] += TEMP[i-1]
    
    for i in range(len(COUNTS)-1, -1, -1):
        TEMP[DATA[i]] -= 1
        COUNTS[TEMP[DATA[i]]] = DATA[i]
    
    return COUNTS

lst = [0, 4, 1, 3, 1, 2, 4, 1]
sort_lst = [0] * len(lst)

print(Counting_sort(lst, sort_lst, len(lst)))