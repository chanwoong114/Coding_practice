N, M, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = list(map(int, input().split()))
dice1 = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1} # 위 찾기
dice2 = {1: [0, 3, 4, 2, 5],
         2: [0, 3, 4, 6, 1],
         3: [0, 6, 1, 2, 5],
         4: [0, 1, 6, 2, 5],
         5: [0, 3, 4, 1, 6],
         6: [0, 3, 4, 5, 2]} # 아래 찾기

for row in range(N):
    if arr[row].count(0) == 1:
        col = arr[row].index(0)
        break

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]
t = 1
r = row
c = col
value = [0]*7
for i in range(k):
    if r+dr[lst[i]]<0 or r+dr[lst[i]]>=N or c+dc[lst[i]]<0 or c+dc[lst[i]]>=M:
        continue
    if arr[r+dr[lst[i]]][c+dc[lst[i]]] != 0:
        value[dice2[t][lst[i]]] = arr[r+dr[lst[i]]][c+dc[lst[i]]]
        arr[r+dr[lst[i]]][c+dc[lst[i]]] = 0
    else:
        arr[r+dr[lst[i]]][c+dc[lst[i]]] = value[dice2[t][lst[i]]]
    t = dice1[dice2[t][lst[i]]]
    print(value[t])
    print(value, t)
    r = r+dr[lst[i]]
    c = c+dc[lst[i]]