class Calculator:
    def __init__(self, n, m):
        self.first = n
        self.second = m

    def add(self):
        return self.first + self.second
    
    def substract(self):
        return self.first - self.second
    
    def multuply(self):
        return self.first * self.second
    
    def divide(self):
        if self.second == 0:
            return '0으로 나눌 수 없습니다.'
        return self.first + self.second
    
q1 = Calculator(1, 1)
print(q1.add())

q2 = Calculator(2, 1)
print(q2.substract())

q3 = Calculator(3, 4)
print(q3.multuply())

q4 = Calculator(4, 0)
print(q4.divide())

# 1 + 2
# 2 – 1
# 3 * 4
# 4 / 0