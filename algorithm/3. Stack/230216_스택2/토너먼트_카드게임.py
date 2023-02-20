def divide(start, end):
    if len(arr[start:end+1]) == 1:
        return (start, arr[start])

    half = (start+end)//2
    first = divide(start, half)
    second = divide(half+1, end)

    if first[1] == 1:
        if second[1] == 2:
            return second
        else:
            return first
    elif first[1] == 2:
        if second[1] == 3:
            return second
        else:
            return first
    else:
        if second[1] == 1:
            return second
        else:
            return first


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    print(f'#{test_case}', divide(0, n-1)[0]+1)