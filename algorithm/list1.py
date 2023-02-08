import sys
input = sys.stdin.readline

n = int(input())
pillar = [list(map(int, input().split())) for _ in range(n)]

pillar.sort(key = lambda x : x[0], reverse=True)
pillar = list(zip(*pillar[::-1]))

for i in range(2):
    pillar[i] = list(pillar[i])

center = pillar[1].index(max(pillar[1]))
minimum = pillar[1][0]
length = pillar[0][0]
size = 0
for i in range(1, center+1):
    if minimum == pillar[1][center]:
        size += minimum * (pillar[0][i] - length)
    if pillar[1][i] > minimum:
        size += minimum * (pillar[0][i] - length)
        length = pillar[0][i]
        minimum = pillar[1][i]

minimum = pillar[1][-1]
length = pillar[0][-1]+1

for i in range(n-2, center-1, -1):
    if pillar[1][i] > minimum:
        size += minimum * (length - (pillar[0][i]+1))
        length = pillar[0][i]+1
        minimum = pillar[1][i]

size += pillar[1][center] * (length - pillar[0][center])

print(size)