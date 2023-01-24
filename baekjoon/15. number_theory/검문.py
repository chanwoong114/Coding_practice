# 2981 : 검문

# M = A-B,B-C의 공약수 이므로 최대 공약수를 구하면 된다.
# 반복횟수를 줄이기 위해 나머지와 몫을 한번에 구해서 반복횟수를 제곱근까지 줄인다.

from math import gcd

N = int(input())
L = [int(input()) for _ in range(N)]

minus = []
answer = []

for i in range(1, len(L)):
    minus.append(L[i]-L[i-1])

prev = minus[0]

for i in range(1, len(minus)):
    prev = gcd(prev, minus[i])

for i in range(2, int(prev**.5)+1):
    if prev%i == 0:
        answer.append(i)
        answer.append(prev//i)

answer.append(prev)

ans = list(set(answer))

ans.sort()

print(*ans)