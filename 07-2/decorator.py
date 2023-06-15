# decorator.py
import time

def elapsed(original_func):   # 기존 함수를 인수로 받는다.
    def wrapper():
        start = time.time()
        result = original_func()    # 기존 함수를 수행한다.
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))  # 기존 함수의 수행시간을 출력한다.
        return result  # 기존 함수의 수행 결과를 리턴한다.
    return wrapper

@elapsed
def myfunc():
    print("함수가 실행됩니다.")

# decorated_myfunc = elapsed(myfunc)  # @elapsed 데코레이터로 인해 더이상 필요하지 않다.
# decorated_myfunc()

myfunc()
