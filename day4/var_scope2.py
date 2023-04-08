# 함수
# 전역 변수의 생성 - 메인 영역에서 생성되고, 값을 공유(저장)
# 전역 변수의 소멸 - 프로그램이 종료되면 소멸

def one_up():
    global x
    x = x + 1
    return x

# 메인 영역
x = 1   # one_up() 함수의 전역변수 선언
print(one_up()) #2
print(one_up()) #3
print(one_up()) #4
print(x)  #4
