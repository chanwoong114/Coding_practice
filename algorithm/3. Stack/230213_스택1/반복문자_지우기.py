# T = int(input())
# for test_case in range(1, T+1):
#     s = str(input())
#     flag = 1
#     while flag:
#         flag = 0
#         for i in range(1, len(s)):
#             if s[i] == s[i-1]:
#                 s = s.replace(s[i]+s[i-1], '', 1)
#                 flag = 1
#                 break
#
#     print(f'#{test_case}', len(s))

T = int(input())
for test_case in range(1, T+1):
    s = str(input())
    stack = []

    for i in s:
        if stack == []:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    print(f'#{test_case}', len(stack))