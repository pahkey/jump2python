f = open('test.txt', 'r')
body = f.read()  # test.txt의 내용을 body 변수에 저장
f.close()

body = body.replace('java', 'python')  # body 문자열에서 "java"를 "python"으로 변경

f = open('test.txt', 'w')  # 파일을 쓰기 모드로 열기
f.write(body)
f.close()
