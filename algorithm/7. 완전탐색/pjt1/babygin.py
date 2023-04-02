def babygin(lst):
    new_lst = sorted(lst)
    if new_lst[0] == new_lst[1] - 1 == new_lst[2] - 2:
        return True
    elif new_lst[0] == new_lst[1] == new_lst[2]:
        return True
    else:
        return False

def per(k):
    global result
    if len(k) == N:
        front = k[:N // 2]
        back = k[N // 2:]
        for i in range(N // 2):
            front[i] = int(ex[front[i]])
            back[i] = int(ex[back[i]])

        if babygin(front) and babygin(back):
            result = True

    for i in range(N):
        if not used[i]:
            used[i] = True
            k.append(i)
            per(k)
            k.pop()
            used[i] = False

N = 6
used = [False] * N
total = set(list(range(N)))
result = False

ex = '124783'
per([])
print(result)
