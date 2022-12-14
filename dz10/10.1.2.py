# Дан многомерный список. Вывести на экран все четные столбцы, у которых первый элемент больше последнего.

A = [
    [1, 6, 8, 5, 4, 0, 3],
    [5, 7, 8, 9, 4, 2, 1],
    [6, 0, 7, 8, 1, 2, 5],
    [5, 7, 2, 7, 5, 2, 1]
]

for i, value_1 in enumerate(A):
    print(*[A[i][j] for j, value_2 in enumerate(value_1) if j % 2 == 0 and A[0][j] > A[len(A)-1][j]])
