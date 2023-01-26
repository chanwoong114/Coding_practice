def fib(m):
    if m == 1:
        return [1,1]
    
    lst = [0] + fib(m-1) + [0]
    
    for i in range(len(lst)-1):
        lst[i] = lst[i] + lst[i+1]

    return lst
    


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    
    print(fib(M)[N])
    