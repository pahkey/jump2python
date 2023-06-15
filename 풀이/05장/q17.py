import itertools
import random

people = ['김승현', '김진호', '강춘자', '이예준', '김현주']
duty = ['청소', '빨래', '설거지']

random.shuffle(people)  # 무작위로 섞는다.
result = itertools.zip_longest(people, duty, fillvalue='휴식')
for r in result:
    print(r)
