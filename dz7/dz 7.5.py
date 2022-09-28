# Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом,
# находящимся на некотором постоянном числе позиций левее или правее него в алфавите. Например, в шифре со
# сдвигом вправо на 3, А была бы заменена на Г, Б станет Д, и так далее. Нужно реализовать шифрование с помощью Python.
# Пользователь вводит строку которую хочет зашифровать и число (сдвиг), нужно с помощью шифра Цезаря ее
# зашифровать и вывести на экран.
# Выполнить задание нужно с помощью цикла for и строк, для получения числового представления символа можно
# использовать ord, а для преобразования числа в строку - chr.

# user_text = input("Enter yout text: ")
# symbol_move = int(input("Enter symbol's shift: "))
# a = 0
# for i in user_text:
#     coded_text = chr(ord(user_text[a]) + symbol_move)
#     a += 1
#     print(coded_text, end="")

user_text = input("Enter yout text: ")
symbol_move = int(input("Enter symbol's shift: "))
for i in user_text:
    if 97 <= ord(i) <= 122:
        coded_text = chr((((ord(i) - 97) + symbol_move) % 26) + 97)
        print(coded_text, end="")
    elif 65 <= ord(i) <= 90:
        coded_text = chr((((ord(i) - 65) + symbol_move) % 26) + 65)
        print(coded_text, end="")
    else:
        exit()
