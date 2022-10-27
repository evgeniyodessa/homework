# Необходимо создать класс Human с атрибутами:
#
# name
# surname
# age
# phone
# address
# Атрибуты должны заполняться в методе __init__
#
# Так-же нужно написать методы:
#
# get_info() - который возвращает словарь в котором находится информация о человеке
# call(phone_number) - который будет выводить "{self.phone} вызывает абонента {phone_number}"
# Нужно создать 3 обьекта класса Human и вызвать у них метод get_info

class Human:
    def __init__(self, name, surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        result = {'name': f'{self.name}', 'surname': f'{self.surname}', 'age': f'{self.age}', 'phone': f'{self.phone}',
                  'address': f'{self.address}'}

        return result

    def call(self, phone_number):
        print(f'{self.phone} is calling {phone_number}')


rooney = Human('Wayne', 'Rooney', 35, '+09379992', 'Odessa, Segedkaya str., 25')
satoshi = Human('Satoshi', 'Nakamoto', 99, '+38067777777', 'Odessa, Altair 2, app. 69')
flemming = Human('Alex', 'Flemming', 18, '+911123456', 'Odessa, Alexandrovsky avenue, 15')

print(rooney.get_info())
print(satoshi.get_info())
print(flemming.get_info())


