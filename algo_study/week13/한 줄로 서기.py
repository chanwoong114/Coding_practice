n = int(input())
people = list(map(int, input().split()))
arr = [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        if arr[j] == 0:
            cnt += 1
        if cnt - 1 == people[i]:
            arr[j] = i + 1
            break

print(*arr)