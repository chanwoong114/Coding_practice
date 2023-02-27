# def hexTodec(s):
#     if s.isdigit():
#         return int(s)
#     else:
#         return ord(s) - ord('A') + 10
#
#
# def decTobin(value):
#     s = ''
#     for j in range(3, -1, -1):
#         s += '1' if value & (1<<j) else '0'
#     print(s)
#         r = value & (1<<j)
#         if r != 0:
#             print(1)
#         else:
#             print(0)
#
#
# def hexTobin(s):
#     # 16진수를 10진수로
#     l = ''
#     for i in s:
#         if i.isdigit():
#             l += i
#         else:
#             l += ord(i) - ord('A') + 10
#
#     # 10진수를 2진수로
#     res = ''
#     for i in range(0, len(l)//4, 4):
#         for j in range(3, -1, -1):
#             res += '1' if l[i:i+4] & (1<<j) else '0'
#     return res
#
# def hexTobin(s):
#     # 16진수를 10진수로
#     if s.isdigit():
#         decV = int(s)
#     else:
#         decV = ord(s) - ord('A') + 10
#
#     # 10진수를 2진수로
#     res = ''
#     for j in range(3, -1, -1):
#         res += '1' if decV & (1<<j) else '0'
#     return res
#
# def hexTobin(s):
#     mapping = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
#                '4': '0100', '5': '0101', '6': '0110', '7': '0111',
#                '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
#                'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
#
#     return mapping[s]
#
#
# #'7329'
# def atoi(s):
#     res = 0
#     for n in s:
#         value = int(n)
#         # value = ord(n) - ord('0')
#         res = res*10 + value
#     return res
#
# def binTodec(s):
#     resD = 0
#     for n in s:
#         value = int(n)
#         resD = resD*2 + value
#
# def binTohex(s):
# #     resD = int(s[0])*8 + int(s[1])*4 + int(s[2])*2 + int(s[3])
#     resD = 0
#     for n in s:
#         value = int(n)
#         resD = resD*2 + value
#
#     if resD < 10:
#         return str(resD)
#     else:
#         return str((resD-10) + ord('A'))

print([(1,2),3] + [4, 5])