import sys
input = sys.stdin.readline

n = int(input())
stack = []
res = [int(input()) for _ in range(n)]

answer = []

i = 1

while res:
    if stack and stack[-1] == res[0]:
        stack.pop()
        res.pop(0)
        answer.append('-')
    else:
        stack.append(i)
        i+=1
        answer.append('+')
    if i>n+1:
        break

if i<n+2:
    for i in answer:
        print(i)
else:
    print('NO')