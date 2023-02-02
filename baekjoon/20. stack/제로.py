import sys
input = sys.stdin.readline

k = int(input())
stack = []
for i in range(k):
    i = int(input())
    if i:
        stack.append(i)
    else:
        stack.pop()

print(sum(stack))