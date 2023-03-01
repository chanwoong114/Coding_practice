list = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]

def all_list_sum(L):
    sumV = 0
    for i in L:
        for j in i:
            sumV += j

    return sumV

print(all_list_sum(list))