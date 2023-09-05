########################################################################################################################
# TODO list comprehension

import random
from typing import Union

# новый массив с квадратами значений другого
list1 = [1, 2, 3, 4, 5]
list2 = []
for i in list1:
    result = i ** 2
    list2.append(result)
print(list2)

# простейший пример
list3 = [i ** 2 for i in [1, 2, 3, 4, 5]]
print(list3)

# новый массив с проверками на чётность
list4 = [1, 2, 3, 4, 5]
list5 = []
for x in list4:
    # if x % 2 == 0:
    #     list5.append(True)
    # else:
    #     list5.append(False)

    # print(x % 2 == 0, type(x % 2 == 0))
    list5.append(x % 2 == 0)
print(list5)

list6 = [x % 2 == 0 for x in list4]
print(list6)

# пример с условием
list7 = ["P", "p", "p", 5, "p", "P", "p"]
list8 = [str(x).isupper() for x in list7 if not isinstance(x, int)]
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
list7 = [{f"key_{i}": i} for i in list5 if i % 2 == 0]
print(list7)

list8 = [" apple ", " banana ", "cherry", "kiwi ", " mango"]
list9 = [str(x).strip() for x in list8 if "i" not in str(x).lower() and len(str(x).strip()) >= 6]
print(list9)

print("Яблоко, банан, груша       , киви      ".split(","), type("Яблоко, банан, груша       , киви      ".split(",")))

list10 = [str(x).strip().lower() for x in "Яблоко, банан, груша       , киви      ".split(",")]
print(list10)

rand1 = random.randint(1, 100)  # 20
print(rand1)

rand2 = random.random()  # 0.12991683412565858 [0, 1]
print(rand2)

rand3 = random.choice([1, 2, 3])  # 3
print(rand3)


# TODO ещё пример
def random_passwrd(length: int, chars="1234567890aewdfseGERWGRWrgkyky6!!!#%^^&!2") -> str:
    if length <= 0 or length > 256 or len(chars) <= 0:
        raise ArithmeticError
    temp_password_string = ""
    while len(temp_password_string) < length:
        temp_password_string += random.choice(chars)
    return temp_password_string


password1 = random_passwrd(length=12)  # eG43#!ya4GGs
print(password1)

names = ["Аня", "Надя", "Катя", "Юля", "Оля"]
print(random.choice(names))  # Надя

list11 = [{"name": random.choice(names) + f" {x}", "age": x} for x in range(1, 100+1)]
print(list11)

list11.sort(reverse=True, key=lambda dict_value: dict_value["age"])
print(list11)

########################################################################################################################

########################################################################################################################
# TODO tuple comprehension

# новый массив с квадратами значений другого
list1 = [1, 2, 3, 4, 5]
list2 = []
for i in list1:
    if i % 2 != 0:
        result = i ** 2
        list2.append(result)
tuple1 = tuple(list2)
print(tuple1)

# простейший пример
tuple2 = (x ** 2 for x in list1 if x % 2 != 0)
print(tuple2, type(tuple2))  # <generator object <genexpr> at 0x00000241537567A0> <class 'generator'>
print(tuple(tuple2), type(tuple(tuple2)))  # (1, 9, 25) <class 'tuple'>
for i in tuple2:
    print(f"Values: {i}")

########################################################################################################################

########################################################################################################################
# TODO dict comprehension

# новый словарь из пар значений
list10 = [["key_1", 1], ["key_2", 2], ["key_3", 3]]
dict1 = {}
for k, v in list10:
    dict1[k] = v
print(dict1)  # {'key_1': 1, 'key_2': 2, 'key_3': 3}

# простейший пример
list11 = [["key_1", 1], ["key_2", 2], ["key_3", 3]]
dict2 = {k: v for k, v in list11}
print(dict2)  # {'key_1': 1, 'key_2': 2, 'key_3': 3}

########################################################################################################################
