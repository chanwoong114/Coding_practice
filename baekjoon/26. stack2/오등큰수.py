from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
cntlst = Counter(lst)
arr = [-1]*n
stack = [0]

for i in range(1, n):
    while stack and cntlst[lst[stack[-1]]] < cntlst[lst[i]]:
        arr[stack.pop()] = lst[i]
    stack.append(i)

print(*arr)