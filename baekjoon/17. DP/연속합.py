N = int(input())
lst = list(map(int, input().split()))

sum_list = [lst[0]]

for i in range(len(lst)-1):
    sum_list.append(max(sum_list[i]+lst[i+1], lst[i+1]))

print(max(sum_list))