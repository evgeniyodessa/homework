# Напишите программу где пользователь вводит число - count, а программа выводит count чисел фибоначчи.
count = int(input("Enter amount of Fibonacci's' numbers: "))
if count == 1:
    print(0)
    exit()
a = 0
print(a)
b = 1
print(b)

for i in range(count - 2):
    b = a + b
    a = b - a
    print(b)
