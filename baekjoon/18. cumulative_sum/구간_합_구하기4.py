import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

lst = [0] + lst

for i in range(1, n+1):
    lst[i] = lst[i] + lst[i-1]


for _ in range(m):
    i, j = map(int, input().split())
    print(lst[j]-lst[i-1])