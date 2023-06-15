# decorator2.py
import time

def elapsed(original_func):   # 기존 합수를 인수로 받는다.
    def wrapper(*args, **kwargs):   # *args, **kwargs 매개변수 추가
        start = time.time()
        result = original_func(*args, **kwargs)  # 전달받은 *args, **kwargs를 입력파라미터로 기존함수 수행
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))  # 수행시간을 출력한다.
        return result  # 함수의 결과를 리턴한다.
    return wrapper

@elapsed
def myfunc(msg):
    """ 데코레이터 확인 함수 """
    print("'%s'을 출력합니다." % msg)

myfunc("You need python")
