n = int(input('enter amount of files: '))
keys = {'write': 'W', 'read': 'R', 'execute': 'X'}
A = {}
for i in range(n):
    a = input('enter file name: ')
    b = input('enter permission for file: ')
    A[a] = b
print(A)
m = int(input('enter amount of files for checking permissions: '))
for i in range(m):
    c = input('enter permission for file: ')
    d = input('enter file name: ')
    if keys[c] in A[d]:
        print('ok')
    else:
        print('access denied')
