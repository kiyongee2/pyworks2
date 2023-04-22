# 모듈
import datetime

# 날짜와 시간 출력 방법
now = datetime.date.today()
print(now)

# 일 수 계산(퇴사일 - 입사일)
start_day = datetime.date(2022, 1, 1)
end_day = datetime.date(2022, 12, 31)
passed_time = end_day - start_day
print(passed_time)
print(f'근무기간 : {passed_time.days}일')

# 시간 측정
# time 모듈 - time.time() -> 초
import time
"""
start = time.time()
#print(start)
#print(round(start/(365*24*60*60))) # 53년

for i in range(1, 1000001):
    print(i)
end = time.time()
print(f'수행시간 : {end-start:.2f}초')
"""
# random 모듈
# 정수- random.ranint(1, 6)
# 리스트 - random.choice(리스트)
import random

num1to10 = random.randint(1, 10)
print(num1to10)

장바구니 = ['계란', '생수', '오렌지', '커피']
#print(장바구니[0])
#print(장바구니[-1])
품목 = random.choice(장바구니)
print(품목)

# math 모듈
# 올림 - math.ceil(), 내림(버림)- math.floor()
# 제곱근 - math.sqrt(), 원주율 - math.pi

# 내장 함수
# 반올림 - round(), 절대값 - abs()
import math

print(math.ceil(15.34)) # 16
print(math.floor(15.34)) # 15
print(round(15.64))  # 16







