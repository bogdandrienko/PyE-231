########################################################################################################################
# TODO list comprehension
import random
import time

# новый массив с квадратами значений другого
list1 = [1, 2, 3, 4, 5]
list2 = []  # [1, 4, 9, 16, 25]
for i in list1:
    result = i ** 2
    list2.append(result)
print(list2)

# простейший пример
list3 = [i ** 2 for i in list1]
print(list3)  # [1, 4, 9, 16, 25]
# синтаксический сахар - уменьшать количество кода

# новый массив с проверками на чётность
list4 = [1, 2, 3, 4, 5]
list5 = []  # [False, True, False, True, False]

for x in list4:
    # if x % 2 == 0:
    #     list5.append(True)
    # else:
    #     list5.append(False)
    list5.append(x % 2 == 0)
print(list5)

list6 = [num % 2 == 0 for num in list4]
print(list6)

# пример с условием
list7_1 = ["P", "p", "p", 5, "p", "P", "p"]
list7 = ["P", "p", "p", "p", "P", "p"]
list8 = [
    f"{x}_"
    for x in list7_1
    if isinstance(x, str) and not x.isupper()
]
print(list8)

# пример для генерации массива словарей
list5 = [1, 2, 3, 4, 5]
list6 = []
for i in list5:
    if i % 2 != 0:
        result = {f"key_{i}": i}
        list6.append(result)
print(list6)

# пример для генерации массива словарей
list7 = [{f"key_{i}": i} for i in list5 if i % 2 != 0]
print(list7)

list8 = [" apple ", " banana ", "cherry", "kiwi ", " mango"]
list9 = [
    x.strip()  # то, что делаем с объектом и какой ложим внутрь "нового" массива
    for x in list8  # объявление переменной и "по чему" проходим циклом
    if x.find("an") >= 0  # условие, которые применяется для фильтрации
]
print(list9)

list10 = [str(x).strip().lower() for x in "Яблоко, банан, груша       , киви      ".split(",")]
print(list10)

import random

print(random.randint(1, 10000))  # 23
res = random.random()
print(res)  # 0.3949273900474488 | 0.0 - 1.0
print(int(res * 100), "%")  # 0.3949273900474488 | 0.0 - 1.0

list12 = [x for x in range(1, 1000 + 1)]
print(random.choice(list12))
print(random.choice("abcde"))



str5 = "p"
numbers = ['1', '2', '3', '4', '5']
str6 = "$ ".join(numbers)  # 1$ 2$ 3$ 4$ 5
# join == "".list -> str
print(str6)

str_new = "apple, banana, mango".split(',')
print(str_new)  # ['apple', ' banana', ' mango']
# split == str -> list


# Практика 1-> реализовать функцию(chars: str, length: int)-генератор пароля
# нужной сложности, из заданных символов
# 2 -> создать тысячу таких паролей в текстовый файл


def make_password(chars: str, length: int) -> str:
    if length < 1:
        raise Exception(f"length is {length}")
    password = ""
    for _ in range(1, length + 1):
        new_char = random.choice(chars)
        password += new_char
    return password
    # return "".join([random.choice(chars) for _ in range(length)])


def make_password2(chars: str, length: int) -> str:
    if length < 1:
        raise Exception(f"length is {length}")
    password = ""
    # while len(password) < length:
    while True:
        if len(password) >= length:
            break
        password += random.choice(chars)
    return password


def make_passwords(count: int) -> bool:
    try:
        with open("password.txt", mode="w", encoding="utf-8") as file:
            for j in range(1, count + 1):
                new_password = make_password("111111111111111111111123456789!@#$%ABCDEFGHabcdefgh", 16)
                file.write(f'{new_password}\n')
    except Exception as error:
        print(error)
        return False
    else:
        return True


print(make_passwords(1200))

names = ["Аня", "Надя", "Катя", "Юля", "Оля"]
print(random.choice(names))  # Надя

########################################################################################################################

########################################################################################################################
# TODO tuple comprehension

list1 = [1, 2, 3, 4, 5]

# простейший пример
tuple2 = (x ** 2 for x in list1)
print(type(tuple2), tuple2)  # <class 'generator'> <generator object <genexpr> at 0x000001BF14428040>
for j in tuple2:
    print(j)

# list comp -> [1, 2, 3, 4, 5] -- for V
# todo list comp - хранит весь объект в оперативной памяти
var1 = 111
var2 = {"name": "Python", "name1": "Python", "name2": "Python"}
import sys
print(var1, sys.getsizeof(var1))  # 28 byte
print(var2, sys.getsizeof(var2))  # 184 byte
# 28 * 10 = 280 byte
#           28 0000 byte == 280 kilobyte
#           28 000 000 byte == 28 megabyte
#           28 000 000 000 byte == 28 gigabyte
print("\n\n\n\n\n********\n\n\n\n")

count = 100000000
count2 = 20000000

# list2 = [x ** 2 for x in range(1, count)]
# print(sys.getsizeof(list2))  # 835 128 600 byte
# sum1 = 0
# for j in list2:
#     sum1 += j
# print(sum1)  # 333333328333333350000000
# ЭКОНОМИТ СКОРОСТЬ ВЫПОЛНЕНИЯ, за счёт памяти

tuple2 = (x ** 2 for x in range(1, count))
print(sys.getsizeof(tuple2))  # 208 byte
sum1 = 0
for j in tuple2:
    sum1 += j
print(sum1)  # 333333328333333350000000
# ЭКОНОМИТ ОПЕРАТИВНУЮ ПАМЯТЬ, за счёт скорости выполнения

# tuple comp -> generator -- for V
# todo tuple comp - "не помнит" предыдущий и "не знает" следующий, есть только текущий

time.sleep(20.0)
