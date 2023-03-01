
# 1부터 주어진 숫자만큼 제네레이터 값을 넣는다
# 각 자리수 + n 

def fn_d(n):
    L = []

    for i in str(n):
        L.append(int(i))

    return n+sum(L)

# 셀프넘버가 숫자들이므로 리스트에 추가

def is_selfnumber(n):
    non_self =[]
    for i in range(n):
        non_self.append(fn_d(i))

    if n in non_self:
        # 리스트에 있다면 셀프넘버가 아님
        print('self_number가 아닙니다.')
        return
    else:
        print('self_number입니다.')
        return
    
N = int(input())

is_selfnumber(N)
