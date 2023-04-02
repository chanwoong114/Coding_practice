# def hoare(l, r):
#     p = l
#     lp = l + 1
#     rp = r
#     while lp <= rp:
#         while lp <= rp and lst[lp] <= lst[p]:
#             lp += 1
#         while lp <= rp and lst[rp] >= lst[p]:
#             rp -= 1
#         if lp < rp:
#             lst[lp], lst[rp] = lst[rp], lst[lp]
#
#     lst[p], lst[rp] = lst[rp], lst[p]
#
#     return rp
#
#
# def lomuto(l, r):
#     p = r
#     i = l-1
#     for j in range(l, r):
#         if lst[j] < lst[p]:
#             i += 1
#             lst[i], lst[j] = lst[j], lst[i]
#
#     i += 1
#     lst[i], lst[p] = lst[p], lst[i]
#
#     return i
#
# def quicks(l, r):
#     if l < r:
#         # p = hoare(l, r)
#         p = lomuto(l, r)
#         quicks(l, p - 1)
#         quicks(p + 1, r)
#
#
# lst = [3, 2, 4, 6, 9, 1, 8, 7, 5]
# quicks(0, 8)
# print(lst)

def merge(left, right):
    result = []
    lp = 0
    rp = 0

    while lp < len(left) and rp < len(right):
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

    middle = len(lst)//2
    left = lst[:middle]
    right = lst[middle:]

    left = mergeS(left)
    right = mergeS(right)

    return merge(left, right)


lst = [69, 10, 30, 2, 16, 8, 31, 22]
res = mergeS(lst)
print(res)