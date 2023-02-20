# def permutation(result):
#     if len(result) == n:
#         if sum(result) == 10:
#             temp = [i for i in result]
#             lst.append(temp)
#             return
#     for i in range(len(arr)):
#         if not result:
#             result.append(arr[i])
#             permutation(result)
#             result.pop()
#         else:
#             if result[-1] < arr[i]:
#                 result.append(arr[i])
#                 permutation(result)
#                 result.pop()
#
# arr = [1,2,3,4,5,6,7,8,9,10]
# lst = []
# arr = [1,2,3,4]
# n = 2
# ans = []
#
# def combi(arr, k):
#     if k == len(arr):
#         if len(ans) == 2:
#             temp = [i for i in ans]
#             lst.append(temp)
#         return
#
#     ans.append(arr[k])
#     combi(arr, k+1)
#     ans.pop()
#     combi(arr, k+1)
#
# combi(arr, 0)
# print(lst)



#
# for n in range(1, 11):
#     permutation([])
# print(*lst)
#
# permutation([])
#
# print(*lst)


# exp = '2+3*4/5'
#
# goal = '234*5/+'
# isp = {'+' : 1, '-' : 1, '*':2, '/':2}
# stack = []
#
# for c in exp:
#     if c.isdigit():
#         print(c)
#     else:
#         if stack and isp[stack[-1]] > isp[c]:
#             print(stack.pop())
#             stack.append(c)
#         else:
#             stack.append(c)
#
# while stack:
#     print(stack.pop())

# exp2 = '(6+5*(2-8)/2)'
# isp = {'+':1, '-':1, '*':2, '/':2, '(':3}
#
# goal = '6528-2/*+'
# stack = []
# for c in exp2:
#     if c.isdigit():
#         print(c)
#     elif c == ')':
#         while stack and stack[-1] != '(':
#             print(stack.pop())
#         stack.pop()
#     else:
#         if stack and isp[stack[-1]] > isp[c]:
#             stack.append(c)
#         else:
#             stack.append(c)
#
# while stack:
#     print(stack.pop())

# exp2 = '(6+5*(2-8)/2)'
# def step1(exp):
#     isp = {'+':1, '-':1, '*':2, '/':2, '(':0}
#     icp = {'+':1, '-':1, '*':2, '/':2, '(':3}
#     goal = '6528-2/*+'
#     stack = []
#     result = []
#     for c in exp2:
#         if c.isdigit():
#             print(c)
#         elif c == ')':
#             while stack and stack[-1] != '(':
#                 print(stack.pop())
#             stack.pop()
#         else:
#             if stack and isp[stack[-1]] > icp[c]:
#                 print(stack.pop())
#                 stack.append(c)
#
#             else:
#                 stack.append(c)
#
#     while stack:
#         print(stack.pop())
#
# step1(exp2)
# def cal(v1, v2, op):
#     if op == '+':
#         return v1 + v2
#     elif op == '-':
#         return v1 - v2
#     elif op == '*':
#         return v1 * v2
#     else:
#         return v1 // v2
#
# def step2(exp):
#     st = []
#     for c in exp:
#         if c.isdigit():
#             st.append(int(c))
#         else:
#             v2 = st.pop()
#             v1 = st.pop()
#             st.append(cal(v1, v2, c))
#     return st.pop()
#
# print(step2('6528-2/*+'))

# nums = [1,2,3]
# n = 3
# a = [-1]*n
#
# def construct_candidates(c):
#     c[0] = 0
#     c[1] = 1
#     return 2
#
# def backtrack(a, k):
#     c = [-1]*2
#     if k == n:
#         print(a)
#         return
#
#     nc = construct_candidates(c)
#     for i in range(nc):
#         a[k] = c[i]
#         backtrack(a, k+1)
#
# backtrack(a, 0)
#
#
# def construct_candidates2(c, k):
#     pos = 0
#     for i in range(n):
#         if i not in a[0:k]:
#             c[pos] = i
#             pos += 1
#     return 2
#
#
# def backtrack2(a, k):
#     c = [-1] * n
#     if k == n:
#         print(a)
#         return
#
#     nc = construct_candidates2(c, k)
#     for i in range(nc):
#         a[k] = c[i]
#         backtrack2(a, k + 1)
#
#
# backtrack2(a, 0)

# nums = [1,2,3,4,5,6,7,8,9,10]
# n = 10
# c = []
# a = [-1]*n
#
# def partial(k, curs):
#     if curs>10:
#         return
#     if len(c) == 5:
#         print(c)
#         return
#
#     c.append(nums[k])
#     partial(k+1, curs)
#     c.pop()
#     partial(k+1, curs + nums[k])
#
#
# partial(0, 0)

a = [[0,0], [0,0]]
a[1] = [1,1]
print(a)