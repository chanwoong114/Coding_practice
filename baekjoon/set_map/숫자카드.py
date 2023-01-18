# 10815 : 숫자카드
import sys
input = sys.stdin.readline

N = int(input())
have = list(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))

dic = {}
for i in range(N):
    dic[have[i]] = 0

for i in range(M):
    if card[i] not in dic:
        print(0, end=' ')
    else:
        print(1, end=' ')
