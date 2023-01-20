# 10815 : 숫자카드
import sys
input = sys.stdin.readline

N = int(input())
have = list(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))

dic = {}
for i in range(M):
    dic[card[i]] = 0

for i in range(N):
    if have[i] in dic:
        dic[have[i]] += 1

for i in range(M):
    if card[i] in dic:
        print(dic[card[i]], end=' ')
    else:
        print(0, end=' ')
        