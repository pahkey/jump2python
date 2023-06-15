# euc_kr.py
# 1. euc-kr로 작성된 파일 읽기
with open('euc_kr.txt', encoding='euc-kr') as f:
    data = f.read()  # 유니코드 문자열 

# 2. unicode 문자열로 프로그램 수행하기
data = data + "\n" + "추가 문자열"

# 3. euc-kr로 수정된 문자열 저장하기
with open('euc_kr.txt', encoding='euc-kr', mode='w') as f:
    f.write(data)
