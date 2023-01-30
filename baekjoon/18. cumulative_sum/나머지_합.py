# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# lst = list(map(int, input().split()))

# lst = [0] + lst
# remain_lst = [0]*m
# remain_lst[0] = 1


# for i in range(1, n+1):
#     lst[i] = lst[i] + lst[i-1]
#     r = lst[i]%m

#     remain_lst[r] += 1

# count = 0

# for i in remain_lst:
#     count += i * (i-1) //2
# # 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수
# print(count)

import sys

input = sys.stdin.readline
n, m = map(int, input().split())  # n : 숫자 갯수, m : 나눌 수 
num = list(map(int, input().split())) + [0]  # 숫자 입력
r = [0] * m  # 누적합을 m으로 나눴을 때의 나머지가 index이고 그 값에 count

for i in range(n):
    num[i] += num[i - 1]  # 숫자 정보를 누적합으로 갱신
    r[num[i] % m] += 1  # 해당 누적합을 m으로 나눴을 때의 나머지에 해당하는 값에 1추가

cnt = r[0]  # 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수

for i in r:
    cnt += i * (i - 1) // 2

print(cnt)