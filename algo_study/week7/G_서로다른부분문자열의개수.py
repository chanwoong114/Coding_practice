s = str(input())
dic = {}

for i in range(len(s)):
    for j in range(len(s)):
        dic[s[i:j+1]] = 0

print(len(dic) - 1)

