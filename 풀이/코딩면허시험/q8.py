f = open('abc.txt', 'r')
lines = f.readlines()    # 모든 라인을 읽음
f.close()

lines.reverse()          # 읽은 라인을 역순으로 정렬

f = open('abc.txt', 'w')
for line in lines:
    line = line.strip()  # 포함되어 있는 줄 바꿈 문자 제거
    f.write(line)
    f.write('\n')        # 줄 바꿈 문자 삽입
f.close()
