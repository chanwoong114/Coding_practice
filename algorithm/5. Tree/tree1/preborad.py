'''
                    1
                2       3
            4        5       6
        7          8   9   10  11
    12                           13
'''

# s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
# lst = list(map(int, s.split()))
# print(lst)
# tree = [[] for _ in range(14)]

# for i in range(0, len(lst), 2):
#     tree[lst[i]].append(lst[i+1])
# print(tree)

# def preorder(root):
#     print(root)
#     if len(tree[root]):
#         preorder(tree[root][0])
#     if len(tree[root]) == 2:
#         preorder(tree[root][1])
#
# preorder(1)

# def inorder(root):
#     if len(tree[root]):
#         inorder(tree[root][0])
#     if len(tree[root]) == 2:
#         inorder(tree[root][1])
#     print(root)
#
# inorder(1)
# n = 13
#
# leftc = [0]*(n+1)
# rightc = [0]*(n+1)
# parent = [0] * (n+1)
#
# for idx in range(0, len(lst), 2):
#     p = lst[idx]
#     c = lst[idx + 1]
#     parent[c] = p
#     if not leftc[p]:
#         leftc[p] = c
#     else:
#         rightc[p] = c
#
# print(leftc)
# print(rightc)
#
# def preorder2(root):
#     print(root)
#     if leftc[root]:
#         preorder2(leftc[root])
#     if rightc[root]:
#         preorder2(rightc[root])
#
# # preorder2(1)
#
# def preorder3(root):
#     if root:
#         print(root, end=' ')
#         preorder3(leftc[root])
#         preorder3(rightc[root])
#
# preorder3(1)
# print()
#
# def findA(c):
#     while c != 0:
#         print(parent[c])
#         c = parent[c]
#
# findA(10)

lst = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'] + [0]*100
print(lst)
def inorder(rootidx):
    if rootidx < len(lst):
        inorder(rootidx*2)
        print(lst[rootidx])
        inorder(rootidx*2 + 1)

# inorder(1)


def findB(rootidx):
    while rootidx != 0:
        if rootidx//2:
            print(lst[rootidx//2])
        rootidx = rootidx//2

findB(5)
