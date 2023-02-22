from collections import deque
import itertools

T = int(input())
for test_case in range(T):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    cnt = 0

    while True:
        if queue[m] > max(queue) or (m == 0 and queue[m] == max(queue)):
            cnt += 1
            break
        elif queue[m] == max(queue):
            cnt += list(itertools.islice(queue, 0, m+1)).count(queue[m])
            break
        else:
            if queue[0] >= max(queue):
                queue.popleft()
                n -= 1
                cnt += 1
            else:
                queue.append(queue.popleft())

            if m == 0:
                m = n - 1
            else:
                m -= 1
    print(cnt)