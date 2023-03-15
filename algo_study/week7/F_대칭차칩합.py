n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dic_a = {}
dic_b = {}

for i in a:
    dic_a[i] = 1

for i in b:
    dic_b[i] = 1

cnt_a = 0
cnt_b = 0
for i in b:
    if dic_a.get(i, 0):
        cnt_a += 1

for i in a:
    if dic_b.get(i, 0):
        cnt_b += 1

print(n+m-cnt_a-cnt_b)