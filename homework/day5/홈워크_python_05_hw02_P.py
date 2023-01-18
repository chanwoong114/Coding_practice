def fn_d(n):
    L = []

    for i in str(n):
        L.append(int(i))

    return n+sum(L)

def is_selfnumber(n):
    non_self =[]
    for i in range(n):
        non_self.append(fn_d(i))

    if n in non_self:
        print('self_number가 아닙니다.')
        return
    else:
        print('self_number입니다.')
        return
    
N = int(input())

is_selfnumber(N)