import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x>0:
        heapq.heappush(heap, (x, 2))
    elif x<0:
        heapq.heappush(heap, (-x, 1))
    else:
        try:
            a, b = heapq.heappop(heap)
            print(a*((-1)**b))
        except:
            print(0)