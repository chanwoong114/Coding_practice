N = int(input())

dice1 = list(map(int, input().split()))
top = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
side = {0: [1, 2, 3, 4],
        1: [0, 2, 4, 5],
        2: [0, 1, 3, 5],
        3: [0, 2, 4, 5],
        4: [0, 1, 3, 5],
        5: [1, 2, 3, 4]}
dice = [list(map(int, input().split())) for _ in range(N-1)]

maxV = 0
for i in range(6): # 첫번째 주사위
    next = dice1[i] # 윗면 설정
    sumV = 0

    # 옆면 리스트 만들어서 그 중 가장 큰 값 구하기
    sidelist1 = []
    for j in side[i]:
        sidelist1.append(dice1[j])
    sumV += max(sidelist1)

    for k in range(N-1): # 나머지 주사위 반복문(dice)
        sidelist2 = []
        for j in range(6): 
            if dice[k][j] == next: # j번째 값이 전 주사위의 윗면과 동일할 때
                next = dice[k][top[j]] # j와 마주보는 값이 다음 윗면
                for a in side[j]:
                    sidelist2.append(dice[k][a])
                break
        sumV += max(sidelist2)

    if maxV < sumV:
        maxV = sumV
print(maxV)
