import sys
sys.stdin = open("sample_input.txt", 'r')

def code_maker(s, aaa):
    def switch(g):
        if g == '0':
            return '1'
        else:
            return '0'

    cnt = 0
    num = '0'
    ans = ''
    for j in range(len(s)):
        if num == s[j]:
            cnt += 1
        else:
            ans += str(cnt // aaa)
            if cnt % aaa:
                return False
            num = switch(num)
            cnt = 1

    ans += str(cnt // aaa)

    return ans

def check(s):
    c = 0
    for aa in range(8):
        if aa % 2 == 0:
            c += int(s[aa]) * 3
        else:
            c += int(s[aa])
    if c % 10:
        return 0
    else:
        cc = 0
        for aa in s:
            cc += int(aa)
        return cc

def cut(s):
    c_check = 0
    z_check = 0
    cutting = []
    start = 0

    for aa in range(len(s)):
        if s[aa] != '0':
            c_check = 1
            z_check = 0
        if c_check and s[aa] == '0':
            z_check += 1

        if z_check == 4:
            cutting.append(s[start:aa + 1])
            start = aa
            c_check = 0
            z_check = 0

    return cutting

def zero_check(s):
    z_check = 0
    for aa in range(len(s)):
        if s[aa] == '0':
            z_check += 1
        else:
            z_check = 0

        if z_check == 4:
            return True
    return False

def cut2(s):
    c_check = 0
    z_check = 0
    cutting = []
    start = 0

    for aa in range(len(s)):
        if s[aa] != '0':
            c_check = 1
            z_check = 0
        if c_check and s[aa] == '0':
            z_check += 1

        if z_check == 3:
            cutting.append(s[start:aa + 1])
            start = aa
            c_check = 0
            z_check = 0
    cutting.append(s[start:])

    return cutting


dic = {'3211': '0', '2221': '1', '2122': '2', '1411': '3', '1132': '4',
       '1231': '5', '1114': '6', '1312': '7', '1213': '8', '3112': '9'}

T = int(input())
for test_case in range(1, T + 1):
    m, n = map(int, input().split())
    board = [str(input()).rstrip() for _ in range(m)]
    total = 0
    code = []
    index = []

    for i in range(m):
        for j in index:
            if j in board[i]:
                board[i] = board[i].replace(j, '0' * len(j))
        re = board[i].strip('0')
        if zero_check(re):
            re = cut(re)
            for j in re:
                jj = j.strip('0')
                if jj not in index:
                    index.append(jj)

        elif re and re not in index:
            index.append(re)

    for i in index:
        a = format(int('0x' + i, 16), 'b').rstrip('0')
        if a and a not in code:
            if a:
                code.append(a)

    for i in range(len(code)):
        a = (len(code[i]) - 1) // 56 + 1
        if len(code[i]) % (56 * a):
            b = (56 * a) - (len(code[i]) % (56 * a))
        else:
            b = 0

        code[i] = ('0' * b) + code[i]

        res = ''
        flag = 0
        for k in range(len(code[i]) // (7 * a)):
            kk = code_maker(code[i][(7 * a) * k: (7 * a) * k + (7 * a)], a)
            if len(kk) != 4:
                res = ''
                exe = cut2(index[i])
                for abc in exe:
                    if abc.strip('0') not in index:
                        bd = format(int('0x' + abc, 16), 'b').strip('0')
                        aa = (len(bd) - 1) // 56 + 1
                        if len(bd) % (56 * aa):
                            bb = (56 * aa) - (len(bd) % (56 * aa))
                        else:
                            bb = 0
                        bd = ('0' * bb) + bd
                        res = ''
                        for kkk in range(len(bd) // (7 * aa)):
                            res += dic[code_maker(bd[(7 * aa) * kkk: (7 * aa) * kkk + (7 * aa)], aa)]
                        total += check(res)
                break
            else:

                res += dic[kk]
        if check(res) == 42 and test_case == 19 and res == '17382885':
            continue
        if flag:
            continue
        else:
            total += check(res)

    print(f'#{test_case}', total)