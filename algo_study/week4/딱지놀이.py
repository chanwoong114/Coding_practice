T = int(input())
for test_case in range(T):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    n, m = a[0], b[0]
    a, b = a[1:], b[1:]

    card1 = [0]*5
    card2 = [0]*5

    for i in a:
        card1[i] += 1
    for i in b:
        card2[i] += 1

    for i in range(4, 0, -1):
        if card1[i] > card2[i]:
            print('A')
            break
        elif card1[i] < card2[i]:
            print('B')
            break
    else:
        print('D')