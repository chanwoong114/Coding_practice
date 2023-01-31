T = int(input())

for _ in range(T):
    h, w, n = map(int, input().split())

    floor = n%h
    ho = (n-1)//h + 1

    if floor == 0:
        floor = h
        
    print(floor*100+ho)