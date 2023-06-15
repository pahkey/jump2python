f1 = open("test.txt", 'w')
f1.write("Life is too short!")
f1.close() # 열린 파일 객체를 닫는다.

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()
