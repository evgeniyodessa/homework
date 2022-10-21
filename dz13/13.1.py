# Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.

def change(lst: list) -> list:
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


a = [1, 3, 5, 3, 'rfsdfd', 'sdf']
print(change(a))
