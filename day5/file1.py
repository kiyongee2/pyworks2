# 파일 쓰기 - 생성 , 파일 읽기
#open(파일경로, 모드) 모드 - 쓰기 : 'w', 읽기 : 'r'
f = open("c:/pyfile/test.txt", 'w')
f.write("hello\n")  #test.txt에 쓰기
f.write("감사합니다.\n")
# 숫자 쓰기는 안됨 - 숫자를 쓸려면 문자화를 해야함
f.write('12\n')
f.write(str(3.3)+'\n')

f.close()