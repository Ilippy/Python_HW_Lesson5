# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def isPrime(a):
    k = 0
    for i in range(2, int(a ** 0.5) + 1):
        if (a % i == 0):
            return False
    return True

# numb = int(input("Введите число\n"))
# print("yes" if isPrime(numb) else "no")


for i in range(2, 101):
    print(f"yes {i}" if isPrime(i) else f"no {i}")
