# Airplane 클래스 사용
from airplane import Airplane
from dog import Dog

# Airplane 클래스 사용
air = Airplane("제주항공")
print(f'비행사 : {air.brand}')
air.take_off()
air.fly()
air.land()

# Dog 클래스 사용
dog = Dog('해피', '불독')
dog.bark()


