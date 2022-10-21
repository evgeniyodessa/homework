# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно
# последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).


def read_last(lines, file):
    if lines > 0:
        a = open(file, 'r')
        strings = a.readlines()[-lines:]
        for i in strings:
            print(i)
        a.close()
    else:
        print("ошибка! должно быть задано положительное целое число ")


read_last(3, 'test.txt')

