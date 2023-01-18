# 입력 예시
# # mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done

# 출력 예시
# 4.0% 700.0g
total = []
for i in range(5):
    total.append(input(f'{i}. 소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ').split())
    if total[i]==['Done']:
        break

if ['Done'] in total:
    for i in range(len(total)-1):
        for j in range(2):
            total[i][j] = int(total[i][j][:-1])
    total.pop(len(total)-1)
else:
    for i in range(len(total)):
        for j in range(2):
            total[i][j] = int(total[i][j][:-1])

salt_water, water = 0, 0
for i in range(len(total)):
    salt_water += total[i][0] * total[i][1] 
    water += total[i][1]

print(f'{round(salt_water/water, 2)}% {water}g')

