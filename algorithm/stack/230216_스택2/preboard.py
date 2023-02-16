# def f(i, k, s, t): # i 원소, k 집합의 크기, s i~1까지 고려된 원소의 합, t 목표
#     global cnt
#     if i == k:
#         if s == t:
#             for j in range(k):
#                 if bit[j]:
#                     print(a[j], end=' ')
#             print()
#             cnt += 1
#         return
#     else:
#         bit[i] = 1
#         f(i+1, k, s+a[i], t) # a[i] 포함
#         bit[i] = 0
#         f(i+1, k, s, t) # a[i] 미포함
#
# a = [1,2,3,4,5,6,7,8,9,10]
# n = 10
# key = 10
# bit = [0]*n
# cnt = 0
#
# f(0, n, 0, key)
# print(cnt)

# def f(i, k, s, t): # i 원소, k 집합의 크기, s i~1까지 고려된 원소의 합, t 목표
#     global cnt
#     global fcnt
#     fcnt += 1
#
#     if s>k: # 고려한 원소의 합이 찾는 합보다 큰경우
#         return
#     elif s == t: # 남은 원소를 고려할 필요가 없는 경우
#         cnt += 1
#         return
#     elif i == k: # 모든 원소 고려
#         if s == t:
#             for j in range(k):
#                 if bit[j]:
#                     print(a[j], end=' ')
#             print()
#             cnt += 1
#         return
#     else:
#         bit[i] = 1
#         f(i+1, k, s+a[i], t) # a[i] 포함
#         bit[i] = 0
#         f(i+1, k, s, t) # a[i] 미포함
#
# a = [1,2,3,4,5,6,7,8,9,10]
# n = 10
# key = 10
# bit = [0]*n
# cnt = 0
# fcnt = 0
#
# f(0, n, 0, key)
# print(cnt, fcnt)

# 순열
nums = [20, 30, 40]

def per(k):
    if k == n:
        print(a)
        for i in range(n):
            idx = a[i]
            print(nums[idx], end=' ')
        print()
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            a[k] = i
            per(k+1)
            visited[i] = False

n = 3
a = [-1] * n
visited = [False] * n
per(0)