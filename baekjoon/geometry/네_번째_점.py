# 3009 : 네 번째 점

# 점의 위치를 생각한다?
# 점을 1234를 정해서 그 위치에 맞는값 변환

square = []
dic1 = {}
dic2 = {}

for _ in range(3):
    square.append(list(map(int, input().split())))

for i in range(3):
    dic1[square[i][0]] = dic1.get(square[i][0], 0) + 1
    dic2[square[i][1]] = dic2.get(square[i][1], 0) + 1

s1 = [k for k,v in dic1.items() if v == 1]
s2 = [k for k,v in dic2.items() if v == 1]

print(*s1, *s2)

# 30 20 
# 30 10 
# 10 20 
# 10 10 

# 7 7 
# 7 5
# 5 7 
# 5 5 

# 9 10
# 9 7
# 5 10
# 5 7

# 11 9
# 11 5
# 4 9
# 4 5