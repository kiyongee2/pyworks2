# 4명의 학생의 국어, 영어, 수학 점수
# 리스트안에 딕셔너리가 요소
student = [
    {'name':'이대한', 'kor':80, 'eng':80, 'math':75},
    {'name':'박민국', 'kor':70, 'eng':65, 'math':60},
    {'name':'오상식', 'kor':75, 'eng':70, 'math':50},
    {'name':'최지능', 'kor':70, 'eng':90, 'math':90}
]
print("=== 학생의 성적표 ===")
print(" 이름  국어 영어 수학")
for std in student:
    # print(std['name'], std['kor'], std['eng'], std['math'])
    print(f'{std["name"]}  {std["kor"]}  {std["eng"]}  {std["math"]}')

print("=== 개인별 총점과 평균 ===")
print(" 이름 총점 평균")
for std in student:
    total = std["kor"] + std["eng"] + std["math"]  # 이대한 - 80+80+75
    avg = total / 3 # 평균
    print(f'{std["name"]} {total} {avg:0.2f}')