# return이 있는 함수
# 제곱수를 계산하는 함수
# 매개 변수가 1개인 함수
def square(x):
    return x * x

print(square(5))

# 1이 증가하는 함수
def one_up(x):
    x = x + 1
    return x

print(one_up(20))

# 매개 변수가 2개 있는 함수
# 두 수의 차를 구하는 함수
def sub(x, y):
    minus = x - y
    return minus

# 두 수의 합을 구하는 함수(add()함수 정의)
def add(x, y):
    plus = x + y
    return plus

# 호출
val = sub(4, 7)
val2 = add(4, 7)
print("두 수의 차 = {0}".format(val))  #-3
print("두 수의 합 = {0}".format(val2)) #11












