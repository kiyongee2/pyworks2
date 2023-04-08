# 절대값을 계산하는 함수

def myabs(x):
    if x < 0:
        return -x
    else:
        return x

print(myabs(4)) #4
print(myabs(-1)) #1
print(abs(-1))  #1

# 1 ~ 30 까지의 자연수 중 배수를 출력, 배수의 개수 구하기
def times(x):
    for i in range(1, 31):
        # 3의 배수 : 3으로 나누어 떨어지는 수(나머지가 0)
        global count
        if i % x == 0:
            count = count + 1
            print(i, end=' ')
        """
        i=1, 1 % 3 == 0 false
        i=2, 1 % 3 == 0 false
        i=3, 1 % 3 == 0 true   3, 개수 1
        i=4, 4 % 3 == 0 false
        i=5, 5 % 3 == 0 false
        i=6, 6 % 3 == 0 true  3, 6 개수 2개
        ...
        """
count = 0  # 전역 변수(정적(static) 변수)
times(3)
print(f'\n배수의 개수 : {count}')
