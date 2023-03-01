# def getDiv(n):
#     lst = []
#     for i in range(1, n+1):
#         if n%i == 0:
#             lst.append(i)
        

#     def mySum(lst):
#         sumv = 0
#         for value in lst:
#             sumv += value
        
#         return sumv
    
#     sumv = mySum(lst)

#     return lst, sumv

# print(getDiv(int(input())))



def dick_list_sum(L):
    sumV = 0

    for i in range(len(L)):
        sumV += L[i]['age']

    return sumV


dick_list = [{'name' : 'kim', 'age' : 12}, {'name' : 'lee', 'age' : 4}]


print(dick_list_sum(dick_list))