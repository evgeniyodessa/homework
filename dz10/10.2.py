# Дан многомерный список в котором находится результат игры в крестики нолики,
# выяснить какой игрок победил (x или o), если никто не победил вывести "Ничья".
# Необходимо учитывать то, что есть разные выигрышные варианты и программа должна их распознавать.

A = [
    ['x', 'x', 'o'],
    ['o', 'o', 'x'],
    ['x', 'o', 'o']
]
if True:
    for i, i_value in enumerate(A):
        a = 0
        for j, j_value in enumerate(i_value):
            if str(A[i][j]) == 'x':
                a += 1
            elif str(A[i][j]) == 'o':
                a -= 1
            if a == 3:
                print("x победил")
                exit()
            elif a == -3:
                print("o победил")
                exit()

    for i, i_value in enumerate(A):
        a = 0
        for j, j_value in enumerate(i_value):
            if str(A[j][i]) == 'x':
                a += 1
            elif str(A[j][i]) == 'o':
                a -= 1
            if a == 3:
                print("x победил")
                exit()
            elif a == -3:
                print("o победил")
                exit()
    a = 0
    for i, i_value in enumerate(A):
        for j, j_value in enumerate(i_value):
            if str(A[i][j]) == str(A[j][i]) == 'x':
                a += 1
            elif str(A[i][j]) == str(A[j][i]) == 'o':
                a -= 1
            if a == 3:
                print("x победил")
                exit()
            elif a == -3:
                print("o победил")
                exit()
    else:
        print("Ничья")

