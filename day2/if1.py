# 조건문(if문) 
# 제한 속도가 50km이상이면 "속도 위반"을 출력하기
"""
limit_speed = 60

if limit_speed >= 50: # 55 >= 50 -> True
    print("속도 위반") # 들여쓰기, 인덴트
"""    

# 조건문(if ~ else문)
# 제한 속도가 50km이상이면 "속도 위반, 과태료 10만원"이고
#  50km 미만이면 "안전 속도 준수"
"""
limit_speed = 49
if limit_speed >= 50:
    print("속도 위반, 과태료 10만원")
else: #limit_speed < 50
    print("안전 속도 준수")
"""
# 시험점수가 60점 이상이면 "합격", 아니면 "불합격" 판정하기
"""
점수 = 55
if 점수 >= 60:
    print("합격")
else:
    print("불합격")
"""
# 어떤 수를 입력받아서 짝수와 홀수를 출력하세요
# %를 나머지 연산자
num = int(input("숫자 입력: "))
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")


    



