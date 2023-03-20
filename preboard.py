lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
       [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]

print(list(zip(*lst[1][::-1])))

for _ in range(3):
    lst = list(zip(*lst[1][::-1]))

print(lst)