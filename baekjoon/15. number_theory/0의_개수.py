from math import factorial

N = int(input())

N = str(factorial(N))

count = 0

for i in range(len(N)-1, -1, -1):
    if N[i] == '0':
        count += 1
    else:
        break

print(count)
