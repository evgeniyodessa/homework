# Напишите программу где пользователь вводит пароль, а программа проверяет сложность пароля и выводит свой
# результат в оценочной шкале от 1 до 5.
# 1 - у пользователя пароль == 'qwerty' or 'admin' или пароль пустой
# 2 - у пользователя только цифры или спец. символы или все буквы в верхнем или нижнем регистре
# 3- у пользователя в пароле соблюдается два условия из (цифры, буква нижнего регистра,
# буква верхнего регистра, спец. символы)
# у пользователя в пароле соблюдается три условия из (цифры, буква нижнего регистра, буква верхнего регистра, спец. символы)
# 5 - у пользователя есть цифры, буквы нижнего и верхнего регистра, спец. символы и длинна пароля больше 8 символов

punct_count = 0
low_count = 0
up_count = 0
dig_count = 0
password = input("enter your password: ")

if password == "qwerty" or password == "admin" or password == "":
    print(1)
    exit()
for i in range(len(password)):
    if str(password[i]).islower():
        low_count += 1
    elif str(password[i]).isupper():
        up_count += 1
    elif str(password[i]).isnumeric():
        dig_count += 1
    else:
        punct_count += 1
if low_count == len(password) or up_count == len(password) or dig_count == len(password) or punct_count == len(
        password):
    print(2)
elif low_count > 0 and dig_count > 0 and up_count == 0 and punct_count == 0:
    print(3)
elif low_count > 0 and up_count > 0 and dig_count == 0 and punct_count == 0:
    print(3)
elif low_count > 0 and punct_count > 0 and dig_count == 0 and up_count == 0:
    print(3)
elif up_count > 0 and punct_count > 0 and dig_count == 0 and low_count == 0:
    print(3)
elif up_count > 0 and dig_count > 0 and punct_count == 0 and low_count == 0:
    print(3)
elif punct_count > 0 and dig_count > 0 and up_count == 0 and low_count == 0:
    print(3)
elif low_count > 0 and dig_count > 0 and up_count > 0 and punct_count == 0:
    print(4)
elif punct_count > 0 and dig_count > 0 and up_count > 0 and low_count == 0:
    print(4)
elif low_count > 0 and dig_count > 0 and punct_count > 0 and up_count == 0:
    print(4)
elif low_count > 0 and punct_count > 0 and up_count > 0 and dig_count == 0:
    print(4)
elif low_count > 0 and dig_count > 0 and up_count > 0 and punct_count > 0 and len(password) > 8:
    print(5)
