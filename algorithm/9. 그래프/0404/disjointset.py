# def findset(x):     # x 가 속한 집합의 대표
#     while x != rep[x]:      # x == rep[x]까지
#         x = rep[x]
#     return x
#
# def union(x, y):    # y의 대표원소가 x의 대표원소를 가리키도록
#     rep[findset(y)] = findset(x)
#     rep[y] = findset(x)
#
# # makeset()
# rep = [i for i in range(6)]

def make_set(x):
    p[x] = x
    rank[x] = 0

def find_set(x):
    if x == p[x]:
        return x
    return find_set(p[x])

def union(x, y):
    # p[find_set(y)] = find_set(x)
    # p[y] = find_set(x)
    xp = find_set(x)
    yp = find_set(y)
    if rank[xp] == rank[yp]:
        p[yp] = xp
        rank[xp] += 1

    elif rank[xp] < rank[yp]:
        p[xp] = yp
    else:
        p[yp] = xp


V = 6
rank = [0] * V
p = [-1] * V
for i in range(V):
    make_set(i)

print(p)
union(2, 3)
union(4, 5)
print(p)
union(3, 5)
print(p)
