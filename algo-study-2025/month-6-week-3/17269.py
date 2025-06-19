# 이름 궁합 테스트

alpha = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

N, M = map(int, input().split());
A, B = map(str, input().split());

arr = []

for i in range(max(N, M)):
    if i < N:
        arr.append(alpha[ord(A[i]) - 65])
    if i < M:
        arr.append(alpha[ord(B[i]) - 65])

for i in range(N + M - 2):
    for j in range(N + M - 1 - i):
        arr[j] = (arr[j] + arr[j+1]) % 10

if arr[0] != 0:
    print(f'{arr[0]}{arr[1]}%')
else:
    print(f'{arr[1]}%')