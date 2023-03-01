n = int(input())
turn = list(map(int, input().split()))

arr = []
for i in range(1, n+1):
    arr.insert(i-1-turn[i-1], i)

print(*arr)