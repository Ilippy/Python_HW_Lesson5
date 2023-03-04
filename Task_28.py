# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def sum(a: int, b: int) -> int:
    if b:
        return sum(a + 1, b - 1)
    return a


a = int(input("Введите а\n"))
b = int(input("Введите b\n"))

print(sum(a, b))
