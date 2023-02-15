def step2(exp):
    global res
    st = []
    for c in exp:
        if c.isdigit():
            st.append(int(c))
        else:
            if len(st) >= 2:
                v2 = st.pop()
                v1 = st.pop()
                st.append(cal(v1, v2, c))
            else:
                res = 0
                return
    if len(st) == 1:
        return st[-1]
    else:
        res = 0
        return

def cal(v1, v2, c):
    if c == '+':
        return v1 + v2
    elif c == '-':
        return v1 - v2
    elif c == '*':
        return v1 * v2
    elif c == '/':
        return v1 // v2

T = int(input())
for test_case in range(1, T+1):
    exp = list(map(str, input().split()))
    exp = exp[:-1]
    res = 1
    ans = step2(exp)
    if res:
        print(f'#{test_case}', ans)
    else:
        print(f'#{test_case} error')

