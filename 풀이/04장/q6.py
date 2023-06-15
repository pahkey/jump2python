user_input = input("저장할 내용을 입력하세요:")
f = open('test.txt', 'a')   # 내용을 추가하기 위해서 'a'를 사용
f.write(user_input)
f.write("\n")               # 입력된 내용을 줄 단위로 구분하기 위해 줄 바꿈 문자 삽입
f.close()
