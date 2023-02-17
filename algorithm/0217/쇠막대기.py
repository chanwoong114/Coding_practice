T = int(input())
for test_case in range(1, T+1):
    st = input()
    ans = cnt = 0
    for i in range(len(st)):
        if st[i] == '(':
            cnt += 1
        else:
            if st[i-1] == '(':
                cnt -= 1
                ans += cnt
            else:
                cnt -= 1
                ans += 1

    print(f'#{test_case}', ans)