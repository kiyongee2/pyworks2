# 파일 리스트 읽기
try:
    # f = open("c:/pyfile/daylist.txt", 'r')
    with open("c:/pyfile/daylist.txt", 'r') as f:
        datalist = f.read()
        print(datalist)
        # f.close()
except:
    print("파일을 찾을 수 없습니다.")