# 리스트의 생성 및 인덱싱
seasons = ['봄', '여름', '가을', '겨울']
print(seasons[0])
print(seasons[-1])

# 리스트 출력
print(seasons)

# 인덱싱과 슬라이싱
print(seasons[0]) #봄
print(seasons[1:3]) #[여름, 가을]

# 전체 요소 출력
for i in seasons:
    print(i)

# 요소의 개수
print('리스트(배열)의 크기:', len(seasons))

# 요소를 수정
seasons[1] = 'summer'
print(seasons[1])
print(seasons)

# 요소 삭제 : del 명령어 사용
del seasons[1]
print(seasons)









