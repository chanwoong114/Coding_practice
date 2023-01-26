grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

def expensive(list):
    price = 0
    for i in list:
        if price < i[1]:
            price = i[1]
            expensive_grain = i[0]


    return expensive_grain

print(expensive(grain_lst))