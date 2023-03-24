n = int(input())
card = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

dic = {}
for i in card:
    dic[i] = dic.get(i, 0) + 1

for i in check:
    print(dic.get(i, 0), end=' ')
