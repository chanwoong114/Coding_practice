# 14425 : 문자열 집합

N, M = map(int, input().split())
words = []
S = []
dic = {}
count = 0

for i in range(N):
    words.append(input())

for i in range(M):
    S.append(input())

for i in words:
    dic[i] = 0

for i in S:
    if i in dic:
        count += 1

print(count)