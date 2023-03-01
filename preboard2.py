n = int(input())
max_idx = 0
min_idx = 9999
arr = [0]*1001

for i in range(n):
  l,h = map(int,input().split())
  arr[l] = h
  max_idx = max(max_idx,l) # 맨 끝점
  min_idx = min(min_idx,l) # 시작점

answer = arr[min_idx]+arr[max_idx]
for i in range(min_idx+1,max_idx):
  max_left = 0
  max_right = 0

  for j in range(min_idx,i): # 왼쪽 탐색
    max_left = max(max_left,arr[j])

  for j in range(i+1,max_idx+1): #오른쪽 탐색
    max_right = max(max_right,arr[j])

  target_h = min(max_left,max_right)

  if arr[i] <= target_h:
    arr[i] = target_h # 높이갱
    answer += target_h
  else:
    answer+=arr[i]

print(answer)