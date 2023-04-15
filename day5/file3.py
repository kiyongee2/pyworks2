# 반복 쓰기
#f = open("c:/pyfile/repeat.txt", 'w')
with open("c:/pyfile/repeat.txt", 'w') as f:
    for i in range(1, 11):
        #숫자 쓰기 안됨-문자로 형변환
        # f.write(str(i))
        data = f'{i}번째 줄입니다.\n'
        f.write(data)
#f.close()