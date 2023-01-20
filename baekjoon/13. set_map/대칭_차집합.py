M, N = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
dic = {}
count = 0

for i in A:
    dic[i] = dic.get(i, 0) + 1

for i in B:
    dic[i] = dic.get(i, 0) + 1

for i in dic:
    if dic[i] == 1:
        count += 1

print(count)