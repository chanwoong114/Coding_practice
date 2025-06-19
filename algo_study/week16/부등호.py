def task(n1, n2, s1):
    if s1 == '<':
        if n1 < n2:
            return True
        else:
            return False

    else:
        if n1 > n2:
            return True
        else:
            return False


def per(s):
    global M_val, m_val

    if len(s) == k+1:
        if s > M_val:
            M_val = s
        if s < m_val:
            m_val = s
        return

    for i in range(10):
        if str(i) not in s and task(int(s[-1]), i, sign[len(s)-1]):
            per(s + f'{i}')



k = int(input())
sign = list(map(str, input().split()))

M_val = '0' * (k+1)
m_val = '9' * (k+1)

for i in range(10):
    per(f'{i}')


print(M_val)
print(m_val)