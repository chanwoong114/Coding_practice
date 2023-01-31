import copy 

n, m = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(n)]
section = [list(map(int, input().split())) for _ in range(m)]
lst_origin = copy.deepcopy(lst)

for i in range(n):
    for j in range(1, n):
        lst[i][j] += lst[i][j-1]

for i in range(m):
    sum_lst = 0
    for j in range(section[i][0]-1, section[i][2]):
        if lst[j][section[i][3]-1] == lst[j][section[i][1]-1]:
            sum_lst += lst_origin[j][section[i][3]-1]
        elif section[i][1]==1:
            sum_lst += lst[j][section[i][3]-1]
        else:
            sum_lst += lst[j][section[i][3]-1]-lst[j][section[i][1]-2]
    print(sum_lst)