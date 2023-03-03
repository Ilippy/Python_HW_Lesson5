# Задача №37. Решение в группах
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def getDigitsReverse(n: int) -> str:
    if n:
        t = input()
        return getDigitsReverse(n-1) + t
    return ""



number = int(input("Введите число\n"))
print(getDigitsReverse(number))