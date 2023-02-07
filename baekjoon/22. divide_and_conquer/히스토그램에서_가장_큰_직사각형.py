import sys
input = sys.stdin.readline

while True:
    n, *lst = map(int, input().split())
    if n == 0:
        break
    lst.append(0)
    ret = 0
    stack = [[0,0]]
    for i in range(n+1):
        while stack[-1][1] > lst[i]:
            tmp_lst = stack.pop()
            tmp_area = 0
            while stack[-1][1] == tmp_lst[1]:
                stack.pop()
            tmp_area = max((i - stack[-1][0]) * tmp_lst[1], (i + 1 - tmp_lst[0]) * tmp_lst[1])
            if tmp_area > ret:
                ret = tmp_area
        stack.append([i+1, lst[i]])
    print(ret)