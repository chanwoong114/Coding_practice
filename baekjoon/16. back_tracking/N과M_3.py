def permutation(lst, r):

    def generate(choice):
        if len(choice) == r:
            print(*choice)
            return
        
        for i in range(len(lst)):                
            choice.append(lst[i])
            generate(choice)
            choice.pop()
    generate([])

N, M = map(int, input().split())
L = [i for i in range(1, N+1)]

permutation(L, M)