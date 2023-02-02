n = int(input())
lst = [tuple(input().split()) for _ in range(n)]

lst = sorted(lst, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in lst:
    print(i[0])