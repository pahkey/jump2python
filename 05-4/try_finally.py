# try_finally.py
try:
    f = open('foo.txt', 'w')
    # 무언가를 수행한다.

    (... 생략 ...)

finally:
    f.close()  # 중간에 오류가 발생하더라도 무조건 실행된다.
