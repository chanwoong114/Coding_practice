import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

oil_price = 0

for i in range(n-1):
    if distance[i]:
        oil_price += distance[i]*price[i]
    else:
        continue
    for j in range(i+1, n-1):
        if price[i] <= price[j]:
            oil_price += distance[j]*price[i]
            distance[j]=0
        else:
            break

print(oil_price)