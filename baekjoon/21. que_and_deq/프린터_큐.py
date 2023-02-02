from collections import deque
import itertools

T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    lst = deque(list(map(int, input().split())))
    cnt = 0

    while True:
        if lst[m] > max(lst) or (m == 0 and lst[m] == max(lst)):
            cnt += 1
            break
        elif lst[m] == max(lst):
            cnt += 1 + list(itertools.islice(lst, 0, m+1)).count(lst[m]) -1
            break
        else:
            if lst[0] >= max(lst):
                lst.popleft()
                n -= 1
                cnt += 1
            else:
                lst.append(lst.popleft())

            if m == 0:
                m = n-1
            else:
                m -= 1
    print(cnt)