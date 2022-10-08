# Дан многомерный список в котором находится результат игры в крестики нолики,
# выяснить какой игрок победил (x или o), если никто не победил вывести "Ничья".
# Необходимо учитывать то, что есть разные выигрышные варианты и программа должна их распознавать.

A = [
    ['x', 'x', 'x'],
    ['x', 'o', 'o'],
    ['o', 'o', 'x']
]
c = 0
for i, i_value in enumerate(A):
    a = 0
    b = 0
    for j, j_value in enumerate(i_value):
        if str(A[i][j]) == 'x':
            a += 1
        elif str(A[i][j]) == 'o':
            a -= 1
        if str(A[j][i]) == 'x':
            b += 1
        elif str(A[j][i]) == 'o':
            b -= 1
        if str(A[0][0]) == str(A[1][1]) == str(A[2][2]) == 'x' or str(A[0][2]) == str(A[2][0]) == str(A[1][1]) == 'x':
            c += 1
        if str(A[0][0]) == str(A[1][1]) == str(A[2][2]) == 'o' or str(A[0][2]) == str(A[2][0]) == str(A[1][1]) == 'o':
            c -= 1
        if a == 3 or b == 3 or c == 3:
            print("x win")
            exit()
        elif a == -3 or b == -3 or c == -3:
            print("o win")
            exit()
else:
    print("Ничья")
