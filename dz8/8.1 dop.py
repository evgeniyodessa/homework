# Задание 1:
# Пользователь вводит слово, если это слово является полиндромом, то вывести '+', иначе '-'

a = input("slovo: ")
if a == a[::-1]:
    print("yes")
else:
    print("no")

# Задание 2:
# Пользователь вводит текст и слово которое нужно найти, если это слово есть в тексте, вывести 'YES', иначе 'NO'

a = input("text: ")
b = input("word: ")
if b in a:
    print("yes")
else:
    print("no")

# Задание 3:
# Пользователь вводит строку. Если она начинается на 'abc', то заменить их на 'www', иначе добавить в конец строки 'zzz'.

a = input("text: ")
if a.startswith("abc"):
    print(a.replace("abc", "www", 1))
else:
    print(f'{a}zzz')

# Задание 4:
# Пользователь вводит текст, удалить в тексте все цифры и вывести строку пользователю.

a = input("text: ")

for i in a:
    if not i.isdigit():
        b = "".join(i)
        print(b, end="")

# Написать валидатор для почты. Пользователь вводит почту, а программа должна проверить, что в почте есть
# символ '@' и '.', и если это так, то вывести "YES", иначе "NO"

a = input("vvod")
if "@" in a and "." in a:
    print('yes')
else:
    print("no")

# Задание 6:
# Пользователь вводит строку в котором есть буквы и цифры, необходимо из этой строки спарсить целое число.