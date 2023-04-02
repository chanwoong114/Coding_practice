def merge(left, right):
    result = []
    lp = 0
    rp = 0

    while lp<len(left) and rp<len(right):
        if left[lp] < right[rp]:
            result.append(left[lp])
            lp += 1
        else:
            result.append(right[rp])
            rp += 1

    result.extend(left[lp:])
    result.extend(right[rp:])

    return result


def mergeS(lst):
    if len(lst) == 1:
        return lst

    m = len(lst)//2
    left = lst[:m]
    right = lst[m:len(lst)]

    left = mergeS(left)
    right = mergeS(right)

    return merge(left, right)


lst = [69, 10, 30, 2, 16, 8, 31, 22]
res = mergeS(lst)
print(res)



def merge(l, r):
    m = (l+r)//2
    result = []
    lp = l
    rp = m+1

    while lp<=m and rp<=r:
        if lst[lp] < lst[rp]:
            result.append(lst[lp])
            lp += 1
        else:
            result.append(lst[rp])
            rp += 1

    while lp <= m:
        result.append(lst[lp])
        lp += 1

    while rp <= r:
        result.append(lst[rp])
        rp += 1

    idx = 0
    for v in result:
        lst[l+idx] = v
        idx += 1


# def mergeS(lst):
def mergeS(l, r):
    if l>=r:
        return

    m = (l+r)//2
    # left = lst[:m]
    # right = lst[m:len(lst)]
    #

    mergeS(l, m)
    mergeS(m+1, r)
    merge(l, r)


lst = [69, 10, 30, 2, 16, 8, 31, 22]
# res = mergeS(lst)
mergeS(0, 7)
print(lst)
