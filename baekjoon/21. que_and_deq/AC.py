import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = list(str(input()))
    n = int(input())
    lst = str(input())
    if n:
        lst = deque(list(map(int, lst[1:-2].split(','))))
    else:
        lst = []
    count = 0
    error = True

    for i in s:
        if i == 'R':
            count += 1
        elif i == 'D':
            if lst:
                if count%2:
                    lst.pop()
                else:
                    lst.popleft()
            else:
                error = False
                break
        
    if error:
        print('[', end = '')
        if lst:
            if count%2:
                for i in range(len(lst)-1, 0, -1):
                    print(lst[i], end='')
                    print(',', end='')
                print(lst[0], end='')
            else:
                for i in range(len(lst)-1):
                    print(lst[i], end='')
                    print(',', end='')
                print(lst[len(lst)-1], end='')
        print(']')

    else: print('error')