# Дан многомерный список. Вывести на экран первый и последний столбцы.

A = [
    [1, 6, 8, 5, 4, 0, 3],
    [5, 7, 8, 9, 4, 2, 1],
    [6, 0, 7, 8, 1, 2, 5],
    [5, 7, 2, 7, 5, 2, 1]
]

for i in range(len(A)):
    a, *other, b = A[i]
    print(a, b)


