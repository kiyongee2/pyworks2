# 리스트의 연산
# 합계, 평균, 개수
score = [70, 80, 60, 100, 90]
count = len(score)
sum_v = 0

for i in score:
    sum_v += i

# 평균 = 합계 / 개수
avg = sum_v / count

print(f"평균: {avg}")

# 합계 구하는 내장 함수
#print(sum(score))
"""
scorelist = [10, 20, 30, 40]

# 요소 추가 (append() 함수 - 맨 뒤에 추가됨)
scorelist.append(50)
print(scorelist)

# 특정 위치에 요소 추가(insert(위치번호, 값))
scorelist.insert(2, 60)
print(scorelist)

# 요소 삭제(pop() - 맨 뒤 요소 삭제)
scorelist.pop()
print(scorelist)

# 요소 개수(len())
print(len(scorelist))
"""



















