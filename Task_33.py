# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def changeMinOnMax(lst: list[int]) -> list[int]:
    mi, ma = min(lst), max(lst)
    # for i in range(len(lst)):
    #     if lst[i] == ma:
    #         lst[i] = mi
    return [mi if i == ma else i for i in lst]


lst = list(map(int, input("Введите массив из цифр через пробел\n").split()))
print(*changeMinOnMax(lst))
