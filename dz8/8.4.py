# Напишите программу где пользователь вводит число symbol_len, а программа генерирует пароль длинной symbol_len.
# Чем выше будет сложность пароля, тем лучше. Сложность пароля буду оценивать по шкале от 1 до 5 из задании #3
import random

symbols = r"""!"# $%&'()*+,-./:;<=>?@[\]^_`{|}~"""
lowercase = 'abcdefghijklmnopqrstuvwxyzabcdefg'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFG'
digits = '0123456789012345678901234567890123'
all_possible = symbols + lowercase + uppercase + digits

symbol_len = input(f'Введите длину пароля: ')

while not symbol_len.isnumeric():
    symbol_len = input(f'Ошибка! Введите целое число: ')
symbol_len = int(symbol_len)
while not int(symbol_len) > 4:
    symbol_len = int(input(f'Ошибка! Введите число больше 4 : '))

for i in range(symbol_len):
    password = "".join(random.choice(all_possible))
    print(password, end="")
