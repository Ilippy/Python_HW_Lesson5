# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def pow(a:int, b:int) -> int:
    if b == 0:
        return 1
    if b == 1:
        return a
    return a * pow(a, b-1)


a = int(input("Введите а\n"))
b = int(input("Введите b\n"))

print(pow(a, b))