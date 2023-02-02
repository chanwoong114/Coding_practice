fomula = input().split('-')
sum_a = 0

if len(fomula) == 1:
    for i in range(len(fomula)):
        a = fomula[i].split('+')
        for j in range(len(a)):
            sum_a += int(a[j])
    print(sum_a)

else:
    a = fomula[0].split('+')
    for j in range(len(a)):
        sum_a += int(a[j])
    for i in range(1, len(fomula)):
        a = fomula[i].split('+')
        for j in range(len(a)):
            sum_a -= int(a[j])
    print(sum_a)