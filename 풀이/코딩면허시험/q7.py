user_input = input("구구단을 출력할 숫자를 입력하세요(2~9):")
dan = int(user_input)       # 입력 문자열을 숫자로 변환
for i in range(1, 10):
    print(i*dan, end= ' ')  # 1줄로 출력하기 위해 줄 바꿈 문자 대신 공백 문자를 마지막에 출력
