# Задание 3:
# Запросить у пользователя 10 чисел и записать их в список A
# Запросить у пользователя число N
# Вывести пользователю сколько в списке A повторяется число N
A = []
count = 0
for i in range(10):
    user_numbers = int(input(f'Введите число №{i + 1}: '))
    A.append(user_numbers)
N = int(input("Введите число: "))
for j in A:
    if j == N:
        count += 1
print(count)
