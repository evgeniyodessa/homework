# Задание 6:
# Запросить у пользователя число N
# Запросить у пользователя N целых чисел и записать их в список A
# Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min и max). Вывести эти числа.

A = []
N = int(input("Введите число: "))
for i in range(N):
    user_number = int(input(f'Введите число №{i + 1}: '))
    A.append(user_number)
sorted(A)
a, *_, b = A
print(a, b)
