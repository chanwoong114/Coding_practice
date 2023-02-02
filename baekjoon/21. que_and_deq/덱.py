from collections import deque
import sys

input = sys.stdin.readline

T = int(input())
deq = deque([])

for i in range(T):
    command = list(map(str, input().split()))

    if command[0] == 'push_back':
        deq.append(command[1])
    elif command[0] == 'push_front':
        deq.appendleft(command[1])
    elif command[0] == 'pop_front':
        if deq:
            a = deq.popleft()
            print(a)
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if deq:
            a = deq.pop()
            print(a)
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(deq))
    elif command[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    else:
        if deq:
            print(deq[-1])
        else:
            print(-1)