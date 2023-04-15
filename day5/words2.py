# 영어 단어장 읽기
import random

try:
    f = open("c:/pyfile/words.txt", 'r')
    # split(구분기호) - 공백문자로 분리
    # 리스트화 됨
    data = f.read().split(' ')
    # print(data[2])
    word = random.choice(data)
    print(word)
except:
    print("파일을 읽을 수 없습니다.")