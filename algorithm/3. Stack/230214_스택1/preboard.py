'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
# V, E = map(int, input().split())
# arr = list(map(int, input().split()))
# adjM = [[0]*(V+1) for _ in range(V+1)]
# for i in range(E):
#     v1, v2 = arr[i*2], arr[i*2+1]
#     adjM[v1][v2] = 1
#     adjM[v2][v1] = 1

V = 7+1
s = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
s = list(map(int, s.split()))
g = [[] for _ in range(V)]

for idx in range(0, len(s), 2):
    v1 = s[idx]
    v2 = s[idx+1]
    g[v1].append(v2)
    g[v2].append(v1)

print(g)

def dfs1(v):
    st = []
    visited = [False] * V
    st.append(v)
    visited[v] = True
    print(v)
    while st:
        for w in g[v]:
            if not visited[w]:
                visited[w] = True
                st.append(v)
                print(w)
                v = w
                break
        else:
            v = st.pop()

dfs1(1)
print('-------------------')
def dfs2(v):
    st = []
    visited = [False]*V
    st.append(v)
    visited[v] = True
    print(v)
    while st:
        v = st.pop()
        if not visited[v]:
            visited[v] = True
            print(v)

        for w in g[v]:
            if not visited[w]:
                st.append(w)

dfs2(1)
print('-------------------')
def dfs3(v):
    st = []
    visited = [False]*V
    st.append(v)
    visited[v] = True
    while st:
        v = st.pop()
        print(v)
        for w in g[v]:
            if not visited[w]:
                st.append(w)
                visited[w] = True

dfs3(1)
print('-------------------')

visited = [False]*V
def dfsr(v): # 재귀 함수로 구현 오래 걸릴 위험이 있다.
    print(v)
    visited[v] = True
    for w in g[v]:
        if not visited[w]:
            dfsr(w)

dfsr(1)
print('-------------------')

gg = [[0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 1, 0, 0],
      [0, 1, 0, 0, 0, 0, 0, 1],
      [0, 0, 1, 0, 0, 0, 1, 0],
      [0, 0, 1, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 1, 1, 0, 1],
      [0, 0, 0, 1, 0, 0, 1, 0]]

def dfs(v):
    st = []
    visited = [False] * V
    st.append(v)
    visited[v] = True
    while st:
        v = st.pop()
        print(v)
        for idx in range(V):
            if gg[v][idx] and not visited[idx]:
                st.append(idx)
                visited[idx] = True

dfs(1)