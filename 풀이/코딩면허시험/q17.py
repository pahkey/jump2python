import re

p = re.compile("a[.]{3,}b")

print(p.match("acccb"))    # None
print(p.match("a....b"))   # 매치 객체 출력
print(p.match("aaab"))     # None
print(p.match("a.cccb"))   # None
