T = int(input())
for _ in range(T):
    a1, a2, d1, b1, b2, d2 = map(int, input().split())

    point_d = (abs(a1 - b1)**2 + abs(a2 - b2)**2)**.5


    if not point_d and d1 == d2:
        print(-1)
    elif max(d1, d2) == point_d + min(d1, d2) or d1 + d2 == point_d:
        print(1)
    elif max(d1, d2) > point_d + min(d1, d2) or d1 + d2 < point_d:
        print(0)
    else:
        print(2)