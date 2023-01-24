# 11478 : 서로 다른 부분 문자열의 개수

# 문자열 S가 주어졌을 때, 서로 다른 문자열의 개수
# ababc
# 12 : a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc 이중에 중복제거 하면 12개

a = input()
count = 0
dic = {}

for i in range(1, len(a)+1):
    for j in range(1, len(a)+2-i):
        dic[a[j-1:j+i-1]] = 0
        
for i in dic:
    count += 1
    
print(count)