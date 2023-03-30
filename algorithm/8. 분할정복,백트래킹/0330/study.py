def insert(value):
    root = 1
    while Tree[root]:
        if Tree[root] > value:
            root *= 2
        else:
            root = root * 2 + 1

    Tree[root] = value

def search(key, root):
    if not Tree[root]:
        return -1

    if Tree[root] == key:
        return root

    if Tree[root] < key:
        return search(key, root*2+1)
    else:
        return search(key, root*2)

Tree = [0] * 100
# p = 1, c1 = p * 2, c2 = p * 2 + 1
lst = [9, 4, 12, 3, 6, 15, 13, 17]

for v in lst:
    insert(v)
print(Tree)
print(search(12, 1))
print(search(14, 1))