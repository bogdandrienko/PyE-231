########################################################################################################################
# TODO MFTI

# TODO каскадное присваивание
a1 = b1 = c1 = 12  # все "переменные" имеют ссылку на один объект
print(a1, b1, c1)

# TODO множественное присваивание
a2, b2, c2 = 1, 2, 3  # все "переменные" имеют ссылку на один объект
# tuple(a2, b2, c2) = tuple(1, 2, 3)
print(a2, b2, c2)

# TODO смена ссылок
x1 = 12
print(x1)
x1 = 13  # имя переменной начинает ссылаться на другой объект,
# предыдущий объект остаётся прежним (т.к. integer неизменяемый тип) и без ссылки "убивается" сборщиком мусора
print(x1)

# TODO обмен переменных
a3 = 12
b3 = 13
print(a3, b3)
a3, b3 = b3, a3
print(a3, b3)

# TODO "множественное" возведение в степень
#        2    1
a4 = 12 ** 3 ** 2

# TODO else в цикле while
index = 1
while index < 10:
    print(index)
    index += 1
else:
    # блок только если цикл успешно завершён (без break)
    print(index)

########################################################################################################################

########################################################################################################################
# TODO EXTRA


# Итераторы
mylist = [1, 2, 3]
for i in mylist:
    print(i)

mylist = [x * x for x in range(3)]
for i in mylist:
    print(i)

# Это удобно, потому что можно считывать из них значения сколько потребуется —
# однако все значения хранятся в памяти, а это не всегда желательно, если у вас много значений.

# Генераторы
mygenerator = (x * x for x in range(3))
for i in mygenerator:
    print(i)


# Генераторы это тоже итерируемые объекты, но прочитать их можно лишь один раз. Это связано с тем,
# что они не хранят значения в памяти, а генерируют их на лету

# Yield это ключевое слово, которое используется примерно как return — отличие в том,
# что функция вернёт генератор

def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i * i


mygenerator = createGenerator()  # создаём генератор
print(mygenerator)  # mygenerator является объектом!
for i in mygenerator:
    print(i)

# корутины

import asyncio


async def count_to_three():
    print("Веду отсчёт. 1")
    await asyncio.sleep(0)
    print("Веду отсчёт. 2")
    await asyncio.sleep(0)
    print("Веду отсчёт. 3")
    await asyncio.sleep(0)


coroutine_counter = count_to_three()
print(coroutine_counter)  # <coroutine object count_to_three at 0x7f5a58486a98>
coroutine_counter.send(None)  # Выведет "Веду отсчёт. 1"
coroutine_counter.send(None)  # Выведет "Веду отсчёт. 2"
coroutine_counter.send(None)  # Выведет "Веду отсчёт. 3"
coroutine_counter.send(None)  # Выбросит ошибку StopIteration

############################################
# виртуальное окружение и наследование глобальных пакетов
# virtualenv --system-site-packages mycoolproject
############################################

#########################################
# запуск скрипта
# python -m pdb my_script.py
#########################################

############################################
# генераторы
from contextlib import contextmanager


@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()


###############################################

############################################
# else в циклах
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n / x)
            break
    else:
        # Цикл не нашел целочисленного делителя для n
        print(n, 'is a prime number')
########################################

####################################
# отладчик python
import pdb


def make_bread():
    pdb.set_trace()
    return "У меня нет времени"


print(make_bread())
######################################

###########################################
# тернарные операторы
is_nice = True
state = "nice" if is_nice else "not nice"


############################################

#######################################################
# распаковка
def profile():
    name = "Danny"
    age = 30
    return name, age


profile_name, profile_age = profile()
print(profile_name)
# Вывод: Danny

print(profile_age)


# Вывод: 30
#####################################################


###########################################################
# магические переменные *args и **kwargs
def test_var_args(f_arg, *argv):
    print("Первый позиционный аргумент:", f_arg)
    for arg in argv:
        print("Другой аргумент из *argv:", arg)


test_var_args('yasoob', 'python', 'eggs', 'test')


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


greet_me(name="yasoob")
###########################################################

######################################################
# enumerate
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)

# Вывод:
# 1 apple
# 2 banana
# 3 grapes
# 4 pear


my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)
# Вывод: [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]
####################################################

###################################################
# map
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))


def multiply(x):
    return (x * x)


def add(x):
    return (x + x)


funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Вывод:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]
####################################################

####################################################
# filter
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Вывод: [-5, -4, -3, -2, -1]
######################################################

######################################################
#
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num

# product = 24


from functools import reduce

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])


# Вывод: 24
##################################################

##################################################
# generator
def generator_function():
    for i in range(10):
        yield i


for item in generator_function():
    print(item)


# Вывод: 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
##################################################

###################################################
# корутины
def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


search = grep('coroutine')
next(search)
# Вывод: Searching for coroutine
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutines instead!")
# Вывод: I love coroutines instead!

########################################################################################################################

import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="31284bogdan",
                              host="127.0.0.1",
                              port="5432",
                              database="django_database")
cursor = connection.cursor()

try:
    connection.autocommit = False
    cursor.execute("insert into zarplata (username, salary) VALUES ('Bogdan5', '666');")
    # cursor.execute("insert into zarplata (username, salary) VALUES ('Bogdan', '666');")

    # print(10 / 0)
    # connection.commit()
except Exception as error:
    print(f"ERROR: {error}")
    connection.rollback()
else:
    pass
finally:
    connection.close()
    cursor.close()

########################################################################################################################

import random
import time

import threading
import multiprocessing
import concurrent.futures
import asyncio

import requests
import aiohttp

# multithreading

# GIL - global intrepreter lock

# url = "https://via.placeholder.com/600/92c952/"  # .png
url = "https://picsum.photos/1920/1080/"  # .png
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


def download_image():
    data = requests.get(url=url, headers=headers)
    # print(data.content)
    # print(data)
    # print(data.status_code)
    # print(len(data.content))  # 384 кб
    with open(f'temp/image{random.randint(1, 1000000)}.jpg', 'wb') as open_file:
        open_file.write(data.content)


async def download_image_async():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as response_instance:
            data = await response_instance.read()
            with open(f'temp/image{random.randint(1, 1000000)}.jpg', 'wb') as open_file:
                open_file.write(data)


def mass_load_image():
    start = time.perf_counter()
    for i in range(1, 10 + 1):
        download_image()
    stop = time.perf_counter()
    print(f"заняло времени: {round(stop - start, 5)}")


def mass_load_image_threads():  #
    start = time.perf_counter()
    new_theads = []
    optimal_workers = int(16 * 32 // 16)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(1, 10 + 1):
            executor.submit(download_image)

    for i in range(1, 10 + 1):
        new_thead = threading.Thread(target=download_image)
        new_theads.append(new_thead)
    # for i in new_theads:
    #     i.start()
    # for i in new_theads:
    #     i.join()  # заставляет основной поток ждать завершения этого потока

    stop = time.perf_counter()
    print(f"заняло времени: {round(stop - start, 5)}")


def mass_load_image_process():
    start = time.perf_counter()
    new_processes = []

    optimal_workers = int(4)
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        for i in range(1, 10 + 1):
            executor.submit(download_image)

    for i in range(1, 10 + 1):
        new_process = multiprocessing.Process(target=download_image)
        new_processes.append(new_process)
    for i in new_processes:
        i.start()
    for i in new_processes:
        i.join()

    stop = time.perf_counter()
    print(f"заняло времени: {round(stop - start, 5)}")


async def mass_load_image_async():
    await asyncio.gather(*[download_image() for i in range(1, 10 + 1)])  # распаковка корутин из list compreh...


def iterator():
    # объект может выполняет повторения .next()
    # mylist = [1, 2, 3]
    # for i in mylist:
    #     print(i)
    #
    # mylist = [x for x in range(1, 3+1)]  # [1, 2, 3]  # выражение создающее list - list comprehension
    # mydict = {value: key for (key, value) in {"key": "value"}.items()}  # выражение создающее list - list comprehension

    # dict2 = {"v": "k"}
    # print(dict2)  # {'v': 'k'}
    # dict2["key1"] = 12
    # print(dict2)  # {'v': 'k', 'key1': 12}
    # del dict2["v"]
    # print(dict2)  # {'key1': 12}

    # генератор - итератор, но прочитать можно только 1 раз, они не хранят в памяти объекты
    # они их вычисляют на лету
    # mygenerator = (x for x in range(1, 3 + 1))  # genexpr <generator object iterator.<locals>.<genexpr> at 0x000002243125AA40>
    # print(mygenerator)
    # for i in mygenerator:
    #     print(i)

    # def create_gen(val: int):
    #     yield val * val  # return - сложное и дорогое вычисление - lazy computing

    # mylist = range(5, 8+1)
    # for j in mylist:
    #     yield j

    # if True:
    #     gen1 = create_gen(5)  # <generator object iterator.<locals>.create_gen at 0x000001FD710FAA40>
    #     print(gen1)
    #     for i in gen1:
    #         print(i)
    # else:
    #     pass

    # корутина
    async def count():
        print("Начало отсчёта")
        await asyncio.sleep(0)
        print("Промежуток отсчёта")
        await asyncio.sleep(0)
        print("Конец отсчёта")

    # coro1 = count()
    # print(coro1)  # <coroutine object iterator.<locals>.count at 0x00000260D486AA40>
    # coro1.send(None)  # до следующего await - Начало отсчёта
    # coro1.send(None)  # до следующего await - Промежуток отсчёта
    # coro1.send(None)  # до следующего await - Конец отсчёта

    # asyncio.run(count())


if __name__ == '__main__':
    # mass_load_image() # 11.60596
    # mass_load_image_threads()  # 1.16204
    # mass_load_image_process()  # 1.41249
    # start = time.perf_counter()
    #
    # try:
    #     asyncio.run(mass_load_image_async())
    # except Exception as error:
    #     pass
    #
    # stop = time.perf_counter()
    # print(f"заняло времени: {round(stop - start, 5)}")

    iterator()
    pass

########################################################################################################################

values = [1, False, 2, "Python", 3]


# for value in values:
#     index = values.index(value)  # берёт первое совпадение!!! если значения не уникальные нельзя!!!
#     print(index-1, value)

# index = 0  # лишний код и расчёты !
# for value in values:
#     index += 1  # лишний код и расчёты !
#     print(index-1, value)

# for index in range(0, len(values)):
#     value = values[index]  # лишний код и расчёты !
#     print(index, value)

# for count, value in enumerate(values):  # map filter (itertools)
#     print(count, value)

# while - бесконечность
# for - временная сложность
# for i in range(1, 100):
#     for j in range(1, 100):
#         for k in range(1, 100):
#             print("")


# map, filter

# map - функция высшего порядка (принимает функцию как аргумент), которая выполняет на массиве ряд одних и тех же операций

def double(val: float) -> float:
    return val ** 2


list1 = [1, 2, 3, 4, 5]
list2 = []
for i in list1:
    result = double(val=i)
    list2.append(result)
print(list2)  # [1, 4, 9, 16, 25]

list3 = [double(val=i) for i in list1]
print(list3)

# прогрев (кэширование) функций

list4 = list(map(double, list1))
print(list4)

# class Map1:
#     def __list__(self):
#         pass

list5 = list(map(lambda y: y ** 2 + 1, list1))
print(list5)

# filter - возвращает новый массив (отфильтрованный), функция которого возвращает True

list6 = list(filter(lambda x: x % 2 != 0, list1))
print(list6)

arr1 = ["Python", "Bogdan", "Teach", "Purum"]
list7 = list(filter(lambda x: "P" in x, arr1))
# list7 = list(filter(lambda x: str(x).find("P") <= -1, arr1))
print(list7)
list8 = []
for i in arr1:
    if "P" in i:
        list8.append(i)
    # else:
    #     continue
print(list8)  # ['Python', 'Purum']

########################################################################################################################

import requests
import aiohttp
import random
import math
import cmath
import cv2
import numpy as np

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}
# data = {"name": "Python is awesome"}
# response = requests.post(
#     url="http://127.0.0.1:8000/test2/",
#     data=data,
#     headers=headers,
# )
# text = "python"
# response = requests.get(
#     url=f"http://127.0.0.1:8000/test2/?text={text}&area=154",
#     params=data,
#     headers=headers,
# )
# print(response)
# print(response.status_code)
# print(response.content)  # b'\x0f\x0e\x0e\x0e\x0e\x0e\x0e'.decode()
# print(response.text)
# print(response.json())

url = "https://picsum.photos/1920/1080/"
response = requests.get(
    url=url,
    headers=headers,
)
image_data = response.content
name = f"temp/image{random.randint(1, 1000000)}.jpg"

with open(name, "wb") as opened_file:
    opened_file.write(image_data)

# https://tproger.ru/translations/opencv-python-guide/
# https://habr.com/ru/post/528144/

# str1 = "Python is awesome"
# print(str1[0:-4:1])

image_data = cv2.imread(name, 0)


# image_data = cv2.resize(image_data, (400, 400))
# image_data = image_data
# im_resize = cv2.resize(image_data, None, fx=1.0, fy=1.0)
# cv2.imwrite(path, image)
#                                   x1 y1   x2  y2

# image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2GRAY)

def encode_image(data):
    # resize inserted image
    data = cv2.resize(data, (1920, 1080))
    # run a color convert:
    data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
    return bytes(data)  # encode Numpay to Bytes string


def decode_image(data):
    # Gives us 1d array
    decoded = np.fromstring(data, dtype=np.uint8)
    # We have to convert it into (270, 480,3) in order to see as an image
    # decoded = decoded.reshape((1920, 1080, 3))
    # return decoded
    # return cv2.imdecode(decoded, cv2.IMREAD_COLOR )


# image_data = decode_image(image_data)
image_data = cv2.cvtColor(image_data, cv2.COLOR_RGB2BGR)
gray_image = cv2.cvtColor(image_data, cv2.COLOR_BGR2GRAY)
# ret, threshold_image = cv2.threshold(image_data, 127, 255, 0)
# cv2.imshow("gray_image", gray_image)
# cv2.imshow("image_data", image_data[10:600, 50:750])
# cv2.imshow("threshold_image", threshold_image)
# cv2.waitKey(0)
cv2.imwrite("temp/new_image.jpg", image_data)

########################################################################################################################

# Что такое глубокая и поверхностная копия
# значение переменной хранится в RAM - оператива
# todo поверхностная копия
from typing import Union

int1 = 12  # ссылка на область в памяти
int2 = int1  # ссылка на переменную

dict1 = {"age": 18}  # ссылка на область в памяти
dict2 = dict1  # ссылка на переменную
dict3 = dict2

dict1["age"] = 17

# print(dict1)
# print(dict2)
# print(dict3)
# todo глубокая копия
dict4 = {"age": 18}  # ссылка на область в памяти
dict5 = dict4.copy()

dict4["age"] = 17
# print(dict4)
# print(dict5)

# JIT - just in time comp...
# Чем файл .рус отличается от .ру?
# TODO .рус - "скомпилированные" файлы .ру

# Linux
# +: $ цена, производительность, безопасность
# -: сложность
# виртуальную машину (vmware / vbox) или полностью установить на пк/ноут

# GIT (open source) - система контроля версий
# git init / git pust / git merge / add....
# GITHUB (microsoft) - облачная система хранения версий под гит (GITLAB)
# создаётся скрытая папка с файлами внутри, которая следит за изменениями всех ваших файлов
# инкрементное - добавляется к предыдущему
# env / node_modules ...

# Что такое *args и **kwargs
# args - позиционные - tuple - кортеж
# kwargs - именные - dict - словарь
print(*(1, 2, 3))  # ручная распаковка
tup1 = (1, 2, 3)
a, b, c = tup1  # автораспаковка


def summing(a1, b1):
    return a1 + b1


def summing2(*args):
    res = 0
    for i in args:
        res += i
    return res


print(summing2(15, 15, 15))


def summing3(**kwargs):
    res = 0
    for k, v in kwargs.items():
        res += v
    return res


# print(summing3(**{"val1": 20, "val2": 20, "val3": 20}))
print(summing3(val1=20, val2=20, val3=20))


def print1(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


print1(12, 1123, name="Привет")


# аннотация типов
# строгой типизацией (c++ / c / c# / java)
# динамической (слабая / сильная) типизацией (javascript / python / php)

def summing7(a2: float, b2: float) -> Union[float, int]:
    return a2 + b2


print(12 / summing7(1, 2))

print(*(12, 15))
print(12, 15)

dict1 = {"age": 12, "age2": 15}
print(dict1["age2"])
for key in dict1.keys():
    print(key)  # age age2
for value in dict1.values():
    print(value)  # 12 15
for item in dict1.items():  # key, value = item
    print(item)  # ("age", 12) ("age2", 15)
print({"age": 12, "age2": 15}.keys())
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(*dict1)
# print(**dict1)
print(age=12, age2=15)


########################################################################################################################
# TODO metaclass

class MyMeta(type):
    def __new__(cls, name, bases, namespace):
        return super().__new__(cls, name, bases, namespace)


class MyClass(metaclass=MyMeta):
    x = 3
