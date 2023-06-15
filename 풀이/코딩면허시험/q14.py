def compress_string(s): 
    _c = ""  # s 문자열 중 현재 진행 중인 문자를 임시 저장하기 위한 변수
    cnt = 0  # 해당 문자가 몇 번 반복했는지 알 수 있는 카운트 변수
    result = ""  # 이 함수의 최종 리턴 문자열(예: a3b2c5a1)
    for c in s:  # 입력받은 문자열 s에서 문자 하나씩 c에 대입
        if c!=_c:  # 현재 진행 중인 문자와 c가 같지 않은 경우, 즉 새로운 문자의 시작
            _c = c  # 현재 진행 중인 문자와 같지 않으므로 현재 진행 문자는 c로 대입
            if cnt: result += str(cnt)  # 새로운 문자이므로 결과 문자열에 이전 문자의 카운트(있을 경우에만)에 해당하는 값을 더해야 함.
            result += c  # 새로운 문자이므로 결과 문자열에 새로운 문자를 더함.
            cnt = 1 # 새로운 문자이므로 카운트는 1로 초기화
        else:  # 현재 진행 중인 문자와 c가 같으므로 카운트 증가
            cnt +=1
    if cnt: result += str(cnt)  # for loop를 벗어날 때 이전 문자의 카운트는 마지막으로 한번 더해야 함
    return result  # 최종 문자열 리턴

print(compress_string("aaabbcccccca"))  # a3b2c6a1 출력