import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
queue = deque([])

for i in range(n):
    command = list(map(str, input().split()))
    if command[0] == 'push':
        queue.append(command[1])
        
    elif command[0] == 'size':
        print(len(queue))
        
    elif command[0] == 'empty':
        if queue:
            print(0)
            
        else:
            print(1)
            
    
    elif queue:
        if command[0] == 'pop':
            print(queue.popleft())
        elif command[0] == 'front':
            print(queue[0])
        else:
            print(queue[-1])
    else:
        print(-1)