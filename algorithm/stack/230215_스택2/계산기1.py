def step1(exp):
    st = []
    res = []
    for c in exp:
        if c.isdigit():
            res.append(c)
        else:
            if st:
                res.append(st.pop())
                st.append(c)
            else:
                st.append(c)
    while st:
        res.append(st.pop())
    return res

def step2(exp):
    st = []
    for c in exp:
        if c.isdigit():
            st.append(int(c))
        else:
            v1 = st.pop()
            v2 = st.pop()
            st.append(v1+v2)

    return st[-1]
for test_case in range(1, 11):
    n = int(input())
    exp = str(input())
    arr = step1(exp)
    exp2 = ''.join(arr)
    print(f'#{test_case}', step2(exp2))