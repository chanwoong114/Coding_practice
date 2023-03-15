# s = str(input())
# dic = {}
#
# for i in range(len(s)):
#     for j in range(len(s)):
#         dic[s[i:j+1]] = 0
#
# print(len(dic) - 1)

import sys

word = sys.stdin.readline().strip()
n = len(word)

cnt = 1
ans = []
a = 0
b = cnt
while cnt <= n:
    wrd = ''
    for i in range(a, b):
        wrd += word[i]
        if len(wrd) == cnt:
            if wrd not in ans:
                ans.append(wrd)
    a += 1
    b += 1
    if b > n:
        a = 0
        cnt += 1
        b = cnt

print(len(ans))