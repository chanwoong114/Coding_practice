T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    people = list(range(1,n))
    for i in range(k):
        for j in range(1, n):
            people[j] = people[j] + people[j-1]
    
    print(people[n-1])