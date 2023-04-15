# 계산기 - 거듭제곱 계산 기능 확장
from calculator import Calculator

class MoreCalculator(Calculator):
    def pow(self):
        return self.x ** self.y

mcal = MoreCalculator(3, 3)
print(mcal.pow())  # 2x2x2=8