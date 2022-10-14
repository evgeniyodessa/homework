n = int(input('enter amount of files: '))
keys = {'write': 'W', 'read': 'R', 'execute': 'X'}
A = {}
for i in range(n):
    a, b = input('enter file name and permission for file: ').split()
    A[a] = b
m = int(input('enter amount of files for checking permissions: '))
for i in range(m):
    c, d = input('enter permission for file and file name: ').split()
    if keys[c] in A[d]:
        print('ok')
    else:
        print('access denied')
