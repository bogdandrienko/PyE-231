########################################################################################################################
# TODO типы данных
from _decimal import Decimal
from random import randint

# имя_переменной =(присваивание) значение_переменной

bool1 = True  # булевы значения в формате Правда/Ложь
bool2 = False  # булевы значения в формате Правда/Ложь

none1 = None  # "пустота" / отсутствие значения

int1 = 12  # целочисленные значения
int2 = 13
print(int1 + int2)

float1 = 12.0  # значения с плавающей точкой
print(int1 + float1)

float2 = -100.00050005000500050005  # значения с плавающей точкой

decimal1 = Decimal(12.0)  # значения с плавающей точкой, но для высокоточных расчётов

str1 = "Python"  # строка - коллекция символьных элементов
str2 = 'Python'  # строка - коллекция символьных элементов
str3 = "I'm"  # строка - коллекция символьных элементов
str3_1 = 'I"m'  # строка - коллекция символьных элементов
str4 = """I''"'m

man
"""  # строка - коллекция символьных элементов

str5 = "Python" + str(12.0)  # конкатенация (сложение строк)
int6 = float("666")
str6 = f"Python {str5}"  # интерполяция (вставка разных переменных в строку)

str7 = "Python \\ \n \t float1"  # спец символы
print(str7)

# "Python".encode() => b"Python"
# b"Python".decode() => "Python"

bytes1 = b"Python"  # байты - коллекция символьных элементов в виде байтов
bytes2 = b'\x01\x02\x03\x04\x05'
# b'\x016А\x02\x03\x04\x05' ASCII (256) vs UTF-8 (N миллионов)

list3 = ["+7 776", 8778]

list1 = [10, True]  # список - коллекция элементов
print(list1)
list1.append(666)
print(list1)

tuple1 = (12, False)  # кортеж - коллекция неизменяемых элементов
print(tuple1)

set1 = {12, False, 12}  # множество - коллекция уникальных элементов
print(set1)
set1.add(True)
print(set1)
set1.add(12)
print(set1)

dict1 = {
    "Имя": "Python",
    "key1": "Анастасия",
    "key2": "Анастасия",
    "970801351179": "А.Б.Н. 1997....",
    "970801351178": "А.Б.Н. 1997....",
    1: "Hi",
}  # словарь - коллекция уникальных элементов в формате ключ-значение
dict2 = {
    "name": "Bogdan",
    "age": 25,
    "arr": [10, True, []],
    "dict1": {
        "name": "Bogdan",
        "age": {
            "name": "Bogdan",
            "age": 25,
            "arr": [10, True, []],
            "dict1": {
                "name": "Bogdan",
                "age": 25,
                "arr": [10, True, []],
            },
        },
        "arr": [10, True, []],
    },
}

dict3 = {"name": "Python"}
int10 = 12.0
print(type(int10))
print(type(dict3), dict3)

INT_CONSTANT = 12  # условно-неизменяемая
print(INT_CONSTANT)

print(INT_CONSTANT / 9)  # 1.0 float
print(INT_CONSTANT // 9)  # 1 int - целочисленное деление

INT_CONSTANT = 13
print(INT_CONSTANT)

is_commit = False  # можно изменить
IS_COMMIT = False  # можно изменить, но не желательно


########################################################################################################################

########################################################################################################################
# TODO действия с переменными

# вывод значение переменной в консоль
print(bool1)  # True

# вывод значение типа переменной в консоль
type_bool1 = type(bool1)  # '<class 'bool'>'
print(type_bool1)
print(type(bool1))  # type_bool1 = type(bool1)

# проверка принадлежности типа данных
print(isinstance(bool1, str))  # False
print(isinstance(bool1, bool))  # True
print(isinstance(12.3, float))  # True

# конвертация типов данных:
float_to_int1 = int(10.5)  # int()
int_to_float1 = float(10)  # float()
str_to_float1 = float("10.2")  # float()
int_to_str1 = str(10.4)  # str()
int_to_bool1 = bool(0)  # bool()
set_to_list1 = list((1, 2, 2, 5))  # list()
# list_to_set1 = set([1, 2, 2, 5])  # set()
list_to_set1 = set(set_to_list1)  # set()
# ...

# получение ввода от пользователя
# str_from_user1 = input("Введите Ваше имя: ")
# print(str_from_user1)

# получение элементов из коллекции
#              0123456789 10 11 12 13 14
source_str1 = "PytHon1! is #wes$me"  # ['P', 'y', 't'...]
#                              -3 -2 -1
print(source_str1[3])
print(source_str1[12])

source_str2 = source_str1[2]
print(source_str2)  # t

print(source_str1[-3])  # $

#               0  1  2  3
source_list1 = [1, 2, 3, 4, 5, 6, 7, 5, 6, 7]
#                       -4

print(source_list1[3])  # 4
print(source_list1[-1])  # 7

#                     [start:stop:step]
source_list2 = source_list1[-5:-2:1]
print(source_list1)
print(source_list1[::-1])
print("Гузель"[::-1])
print(source_list2)

source_list13 = [1, 2, 3, 4, 5, 6, 7, 5, 6, 7]
print(source_list13)
source_list13[2] = 666
print(source_list13)

str13 = "Python"
# todo str13[2] = "$" ! str неизменяемый!
# str13 = "Py$hon"  # переопределение

dict4 = {
    "name": "Bogdan",
    "age": 25,
    "arr": [10, True, []],
}

print(dict4["age"])
print(dict4["arr"])
print(dict4["name"])

dict4["phone"] = "8 777"
print(dict4)
print(dict4["phone"])

del dict4["name"]
print(dict4)
