# 파일 읽기, 예외 처리(오류 처리)
try:
    f = open("c:/pyfile/test.txt", 'r')
    data = f.read()  #읽기는 read() 사용
    print(data)
    f.close()
except:
    print("파일을 찾을 수 없습니다.")