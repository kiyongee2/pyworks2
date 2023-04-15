# 바이너리 파일 쓰기
# 파일경로 - 상대 경로

with open('./output/data.bin', 'wb') as f:
    text = "오늘은 비가 내려요"
    f.write(text.encode())  # 0과 1로 코드화하다

# print("파일을 쓸 수 없습니다.")
# 파일 읽기
with open('./output/data.bin', 'rb') as f:
    data = f.read()
    print(data)
    print(data.decode())