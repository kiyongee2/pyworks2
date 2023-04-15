# 이미지 파일 읽어 와서 쓰기(복사)
try:
    with open("c:/pyfile/flower.jpg", "rb") as f1:
        data = f1.read()
        # print(data)

    # 절대경로 c:/pyworks/day5/output/flower2.jpg
    #  ./ (점이 한개이면 같은 위치, 점이 2개이면 ../ 상위 폴더을 가리킴)
    with open("./output/flower3.jpg", "wb") as f2:
        f2.write(data)
except:
    print("파일을 찾을 수 없습니다.")