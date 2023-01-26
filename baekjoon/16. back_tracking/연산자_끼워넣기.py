N = int(input())
num = list(map(int, input().split()))
operator = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    
    if plus:
        dfs(depth + 1, total + num[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide-1)


dfs(1, num[0], operator[0], operator[1], operator[2], operator[3])
print(maximum)
print(minimum)