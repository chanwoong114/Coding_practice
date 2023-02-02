import sys
input = sys.stdin.readline

while True:
    s = list(input())
    if s[0] == '.':
        break

    stack = []
    res = 1

    for i in s:
        if i == '[':
            stack.append(1)
        elif i == '(':
            stack.append(0)
        elif i == ']':
            if stack:
                a  = stack.pop()
                if a != 1:
                    res = 0
                    break
            else:
                res = 0
                break
        elif i == ')':
            if stack:
                a  = stack.pop()
                if a != 0:
                    res = 0
                    break
            else:
                res = 0
                break
        
    if stack == [] and res:
        print('yes')
    else:
        print('no')