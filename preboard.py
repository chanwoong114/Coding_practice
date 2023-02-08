<<<<<<< HEAD
n = int(input())
k = int(input())

a = k//n + 1
b = k%n + 1

print(a*b)
=======
import sys
input = sys.stdin.readline

s = list(str(input()))
s = s[:-1]
s.sort(reverse=True)

sorted_s = ''

for i in s:
    sorted_s += i
    
print(sorted_s)
>>>>>>> origin/main
