class Stack:
    def __init__(self):
        self.lst = []
    
    def empty(self):
        if self.lst:
            return False
        else:
            return True
        
    def top(self):
        if self.lst:
            return self.lst[-1]
        else:
            return None
    
    def pop(self):
        if self.lst:
            stack_pop = self.lst.pop(-1)
            return stack_pop
        else:
            return None
        
    def push(self, value):
        self.lst.append(value)
        
    def __repr__(self):
        print(self.lst)
        return 


s1 = Stack()

print(s1.empty())

for i in range(5):
    s1.push(i)

s1.__repr__()
print(s1.top())

for i in range(5):
    print(s1.pop())