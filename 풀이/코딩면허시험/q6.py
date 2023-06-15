user_input = input("숫자를 입력하세요: ")
numbers = user_input.split(",")
total = 0

for n in numbers:
    total += int(n)    # 입력은 문자열이므로 숫자로 변환해야 한다.

print(total)
