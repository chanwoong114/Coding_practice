num = int(input())
even_odd = 1
while True:
    if num > even_odd:
        num -= even_odd
        even_odd += 1
    else:
        break

if even_odd%2==0:
    son = num
    mom = even_odd-num+1
else:
    son = even_odd-num+1
    mom = num

print(f'{son}/{mom}')