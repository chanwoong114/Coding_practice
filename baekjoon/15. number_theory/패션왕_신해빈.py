T = int(input())

for _ in range(T):
    N = int(input())
    dic = {}

    for i in range(N):
        kinds, index = map(str, input().split())
        dic[index] = dic.get(index, 0) + 1
    
    cases = 1

    for i in dic.values():
        cases *= (i+1)

    print(cases-1)