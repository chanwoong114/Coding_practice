def step1(exp):
    res = ''
    isp = {'+':1, '*':2, '(':0}
    icp = {'+':1, '*':2, '(':3}
    st = []

    for c in exp:
        if c.isdigit():
            res += c
        elif c == ')':
            while st and st[-1] != '(':
                res += st.pop()
            st.pop()
        else:
            if st and isp[st[-1]] >= icp[c]:
                res += st.pop()
                st.append(c)
            else:
                st.append(c)

    while st:
        res += st.pop()

    return res

def cal(v1, v2, op):
    if op == '+':
        return v1 + v2
    elif op == '*':
        return v1 * v2

def step2(exp):
    st = []
    for c in exp:
        if c.isdigit():
            st.append(int(c))
        else:
            v2 = st.pop()
            v1 = st.pop()
            st.append(cal(v1, v2, c))
    return st.pop()


for test_case in range(1, 11):
    n = int(input())
    s = str(input())

    s = step1(s)
    res = step2(s)
    print(f'#{test_case}', res)