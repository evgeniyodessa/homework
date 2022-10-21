# Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно.
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

def sum_range(start: int, end: int):
    a = 0
    if start > end:
        start, end = end, start
    for i in range(start, end+1):
        a += i
    return a


print(sum_range(2, 6))
