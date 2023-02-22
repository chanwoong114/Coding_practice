import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y = map(int, input().split())
turn = int(input())

x += turn
y += turn

nx = x//n
ny = y//m

if nx%2:
    x = n - x%n
else:
    x = x%n

if ny%2:
    y = m - y%m
else:
    y = y%m

print(x, y)