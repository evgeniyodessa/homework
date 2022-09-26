# Напишите программу где пользователь вводит число - count, а программа выводит count чисел фибоначчи.
count=int(input("vvod"))
a=0
print(a)
b=1
print(b)

for i in range(count):
    b=a+b
    a=b-a
    print(b)
