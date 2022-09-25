# Написать программу которая проверяет что в строке есть хотя бы один пробел, число, буква нижнего и
# верхнего регистра. Если это так, то вывести 'YES', иначе 'NO'

test_string = 'Hello world123'
space_count = 0
low_case_count = 0
up_case_count = 0
digit_count = 0
for symbol in test_string:
    if symbol.isspace():
        space_count += 1
    if symbol.islower():
        low_case_count = +1
    if symbol.isupper():
        up_case_count += 1
    if symbol.isdigit():
        digit_count += 1
if space_count > 0 and low_case_count > 0 and up_case_count > 0 and digit_count > 0:
    print("YES")
else:
    print("NO")
