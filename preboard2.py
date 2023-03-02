 # 백준 2304 번 문제입니다.

n = int(input())
arr = []
for i in range(n):
    v1, v2 = map(int, input().split())
    arr.append([v1, v2])

arr.sort()
m = 0
maxV = []
for i in arr:
    if i[1] > m:
        m = i[1]

for i in range(len(arr)):
    if arr[i][1] == m:
        maxV.append(arr[i])

k = 1
sumV = []
ma = 0

if len(maxV) > 1:
    sumV.append((maxV[len(maxV) - 1][0] + 1 - maxV[0][0]) * maxV[len(maxV) - 1][1])
elif len(maxV) == 1:
    sumV.append(maxV[0][1])

for i in range(1, n):

    if arr[i - 1][1] == maxV[0][1]:

        for j in range(n - 1, i - 2, -1):
            if ma < arr[j][1]:
                ma = arr[j][1]
                maIndex = j

            if ma < arr[j - 1][1]:
                sumV.append((abs(arr[j - 1][0] - arr[maIndex][0])) * arr[maIndex][1])

        break


    elif arr[i - 1][1] <= arr[i][1]:
        sumV.append((arr[i][0] - arr[i - k][0]) * arr[i - k][1])
        k = 1

    elif arr[i - 1][1] > arr[i][1]:
        k += 1
if n == 1:
    sumV.clear()
    sumV.append(arr[0][1])
print(sum(sumV))