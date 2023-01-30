import random

class ClassHelper:
    lst =[]
    def __init__(self, lst):
        random.shuffle(lst)
        for i in lst:
            self.name = i
        ClassHelper.lst = lst

    def pick(self, n):
        random.shuffle(ClassHelper.lst)
        return ClassHelper.lst[:n]
    
    def match_pair(self):
        n = len(ClassHelper.lst)//2
        pair = []
        for i in range(1, n):
            pair.append(ClassHelper.lst[(i-1)*2:i*2])
        pair.append(ClassHelper.lst[i*2:])
        return pair
            



ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])

print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())
