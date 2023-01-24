# 1620 : 나는야 포켓몬 마스터

N, M = map(int, input().split())
words = []
S = []
dic = {}
count = 0

for i in range(N):
    words.append(input())

for i in range(M):
    S.append(input())

for i in range(N):
    dic[words[i]] = i+1
    dic[i+1] = words[i]

for i in S:
    if i.isalpha():
        print(dic[i])

    else:
        print(dic[int(i)])