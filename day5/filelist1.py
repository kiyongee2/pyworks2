# 파일에 리스트 저장하기
day = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
f = open("c:/pyfile/daylist.txt", 'w')
for i in day:
    f.write(i)
    f.write('\n')
f.close()