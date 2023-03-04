# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию


def memoize(func):
    d = {}
    def inner(num):
        if num not in d:
            d[num] = func(num)
        return d[num]
    return inner


@memoize
def fibonacci(n):
    """
    Возвращает n-ое число Фибоначчи
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# fib(5) -> fib(4) + fib(3)
# fib(4) -> fib(3) + fib(2)
# fib(3) -> fib(2) + fib(1)
# fib(2) -> fib(1) + fib(0)
# print(fibonacci(10))
# print(fibonacci(50))
# assert fibonacci(60) == 1548008755920
# assert fibonacci(70) == 190392490709135
# assert fibonacci(80) == 23416728348467685
# assert fibonacci(90) == 2880067194370816120
# assert fibonacci(100) == 354224848179261915075


for i in range(1, 101):
    print(i, fibonacci(i))
