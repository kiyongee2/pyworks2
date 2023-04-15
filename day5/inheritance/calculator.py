# 계산기 - 덧셈, 뺄셈
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

if __name__ == "__main__":
    cal = Calculator(10, 20)
    # print(cal.x, cal.y)
    print(cal.add())    #30
    print(cal.sub())    #-10
