def permutation(lst, r):
    used = [0]*len(lst)

    def generate(choice, used):
        if len(choice) == r:
            print(*choice)
            return
        
        for i in range(len(lst)):
            if not used[i] and (i==0 or lst[i] != lst[i-1] or used[i-1]):
                if len(choice) >= 1 and max(choice) > lst[i]:
                    continue                    
                choice.append(lst[i])
                used[i] = 1
                generate(choice, used)
                used[i] = 0
                choice.pop()
    generate([], used)

N, M = map(int, input().split())
L = [i for i in range(1, N+1)]

permutation(L, M)