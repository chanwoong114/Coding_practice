# 부분 성공

st = input()
test = int(input())

dic = {'a':[0]*len(st),
       'b':[0]*len(st),
       'c':[0]*len(st),
       'd':[0]*len(st),
       'e':[0]*len(st),
       'f':[0]*len(st),
       'g':[0]*len(st),
       'h':[0]*len(st),
       'i':[0]*len(st),
       'j':[0]*len(st),
       'k':[0]*len(st),
       'l':[0]*len(st),
       'm':[0]*len(st),
       'n':[0]*len(st),
       'o':[0]*len(st),
       'p':[0]*len(st),
       'q':[0]*len(st),
       'r':[0]*len(st),
       's':[0]*len(st),
       't':[0]*len(st),
       'u':[0]*len(st),
       'v':[0]*len(st),
       'w':[0]*len(st),
       'x':[0]*len(st),
       'y':[0]*len(st),
       'z':[0]*len(st),}

for ii in range(len(st)):
    dic[st[ii]][ii] = 1

for _ in range(test):
    find, start, end = input().split()
    print(sum(dic[find][int(start):int(end)+1]))
# 성공풀이
import sys
input = sys.stdin.readline

s = input().rstrip()
arr = [[0]*26]
arr[0][ord(s[0])-97] = 1
for i in range(1,len(s)):
    arr.append(arr[-1][:])
    arr[i][ord(s[i])-97] += 1

for _ in range(int(input())):
    c,start,end = list(input().split())
    start,end = map(int,[start,end])
    if start == 0:
        print(arr[end][ord(c)-97])
    else:
        print(arr[end][ord(c)-97]-arr[start-1][ord(c)-97])