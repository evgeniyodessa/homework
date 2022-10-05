# Задание 7:
# Пользователь вводит текст нужно вывести количество цифр в этом тексте
digit_count=0
text=input("Введите текст: ")
for i in text:
    if i.isdigit():
        digit_count+=1
print(digit_count)
