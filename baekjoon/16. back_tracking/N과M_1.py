def permutation(lst, r):
    used = [0]*r

    def generate(choice, used):
        if len(choice) == r:
            print(*choice)
            return
        
        for i in range(len(lst)):
            if not used[i] and (i==0 or lst[i] != lst[i] or used[i-1]):
                choice.append(i)
                used[i] = 1
                generate(choice, used)
                used[i] = 0
                choice.pop()
    generate([], used)

N, M = map(int, input().split())
L = [range(1, N+1)]

permutation(L, M)

