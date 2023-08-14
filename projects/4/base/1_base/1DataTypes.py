###################################################################################################
# TODO типы данных

from decimal import Decimal

# имя_переменной =(присваивание) значение_переменной

bool1 = True  # булевы значения в формате Правда/Ложь
bool2 = False

int1 = 12  # целочисленные значения
int2 = -12

float1 = 12.0555555555555554  # значения с плавающей точкой
float2 = -12.0

decimal1 = Decimal(
    12.0025432532652465436353463565360254325326524654363534635653602543253265246543635346356536)  # значения с плавающей точкой, но для высокоточных расчётов

#       012345
str1 = "Python"  # строка - коллекция символьных элементов
str2 = ""
str3 = 'Awesome'
str4 = "I'm"
str5 = """ I'm

man
"""

str6 = "Python " + "3.12"  # конкатенация (сложение строк)
name = "Bogdan"
age = 26
str7 = f"name is {name}, i'm {age}"  # интерполяция (вставка разных переменных в строку)

# print(str7)

bytes1 = b"Python"  # байты - коллекция символьных элементов в виде байтов
bytes2 = b"\x01\x02\x03\x04\x05"

#        0    1           2             3
list1 = [10, True, [10, True, 12.6], "List"]  # список - коллекция элементов
list2 = []  # пустой список
# print(list2)
# list2.append(123)  # добавить в конец
# list2.append(321)  # добавить в конец
# print(list2)
# list2.pop(1)  # удалил по индексу
# print(list2)

#         0     1
tuple1 = (12, False)  # кортеж - коллекция неизменяемых элементов
tuple2 = (666,)  # кортеж с одним элементом

set1 = {12, False, 12, 12, 12}  # множество - коллекция уникальных элементов
set1.add(12)
set1.add(66)
print(set1)

dict1 = {
    "Имя": "Python"
}  # словарь - коллекция уникальных элементов в формате ключ-значение
dict2 = {
    "name": "Bogdan",
    "age": 25,
    "arr": [10, True, []],
    "dict1": {
        "name": "Bogdan",
        "age": 25,
        "arr": [10, True, []],
    },
}

dict3 = dict(Age=24, Name="Ally")  # создание словаря
print(dict3)

dict4 = {"Age": 24, "Name": "Ally"}  # создание словаря
print(dict4)

INT_CONSTANT = 12  # условно-неизменяемая
# print(INT_CONSTANT)
# INT_CONSTANT = 13
is_commit = False  # можно изменить
IS_COMMIT = False  # можно изменить, но не желательно

HOST_PASSWORD = "password"

###################################################################################################
# TODO действия с переменными


# вывод значение переменной в консоль
print(bool1, 12, 13, True)

# вывод значение типа переменной в консоль
type_bool1 = type(bool1)
print(type_bool1)
print(type(bool1))  # type_bool1 = type(bool1)

# проверка принадлежности типа данных
print(isinstance(bool1, str))  # False
print(isinstance(bool1, bool))  # True
print(isinstance(12, int))  # True


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
str_from_user1 = input("Введите Ваше имя: ")
print(str_from_user1)

# получение элементов из коллекции
#              0123456       -2-1
source_str1 = "Python is awesome"  # ['P', 'y', 't'...]

source_str2 = source_str1[2]
print(source_str2)  # t

source_str3 = source_str1[-2]
print(source_str3)  # m

source_str4 = source_str1[2:6:1]
print(source_str4)

#               0  1  2  3
source_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]]

source_elem2 = source_list1[3]
print(source_elem2)

source_list2 = source_list1[2:5]
print(source_list2)

str13 = "Python"
# todo str13[2] = "$" ! str неизменяемый!
# str13 = "Py$hon"  # переопределение

dict4 = {
    "name": "Bogdan",
    "age": 25,
    "arr": [10, True, []],
}
print(dict4["age"])
print(dict4.get("age", 66))
dict4["money"] = Decimal(12.0)
print(dict4)
del dict4["arr"]
print(dict4)

###################################################################################################
# todo Управление памятью

# "Python" -
# "Bogdan" -

# todo step 1
# str12 - 0
# "Python" - 0
# "Bogdan" - 0

str12 = "Python"
# str12[2] = ""
# todo step 2
# str12 - 1
# "Python" - 1
# "Bogdan" - 0

str12 = "Bogdan"
# todo step 2
# str12 - 1
# "Python" - 1
# "Bogdan" - 1
# reference counting

# since 0.01s
# -> GC -> KILL "Python"

# Garbage Collector - CG - сборщик мусора (процесс в Python, который запускается каждые 0.01с)


# def sum1(a, b):
#     res = a + b
#     return res



# 1. Завести гитхаб и первый репозиторий (скинуть мне ссылку)
# 2. Собрать "выжимку" с 30-70 вакансий, в 1 текстовый файл.
# 3. Пересмотреть видео...(рано)
