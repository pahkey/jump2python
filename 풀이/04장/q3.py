input1 = input("첫 번째 숫자를 입력하세요:")
input2 = input("두 번째 숫자를 입력하세요:")

total = int(input1) + int(input2)      # 입력은 항상 문자열이므로 숫자로 바꾸어 주어야 한다.
print("두수의 합은 %s 입니다" % total)
