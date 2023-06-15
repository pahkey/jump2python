def fib(n):
    if n == 0 : return 0          # n이 0일 때는 0을 반환
    if n == 1 : return 1          # n이 1일 때는 1을 반환
    return fib(n-2) + fib(n-1)    # n이 2 이상일 때는 그 이전의 두 값을 더하여 반환

for i in range(10):
    print(fib(i))
