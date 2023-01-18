# 1764 : 듣보잡

N, M = map(int, input().split())

hear, see = [], []
dic = {}

for i in range(N):
    hear.append(input())

for i in range(M):
    see.append(input())

for i in hear:
    dic[i] = dic.get(i, 0) + 1

for i in see:
    dic[i] = dic.get(i, 0) + 1

hearsee = []

for i in dic:
    if dic[i] == 2:
        hearsee.append(i)

hearsee.sort()

print(len(hearsee))
for i in hearsee:  
    print(i)
