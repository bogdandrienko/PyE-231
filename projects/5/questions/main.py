"""

###########################################################

24. Python - интерпретируемый язык или компилируемый?
- интерпретируемый

###########################################################

25. Какие есть меняющиеся и постоянные типы данных?
-меняющиеся: list, set, dict
- ...

# s1 = "141241"
# s1[2] = ""

###########################################################

26. Что такое область видимости переменных?

l1 = ""
def ex1():
    # global l1
    l1 = "12313"
    print(l1)

print(l1)

###########################################################

27. Что такое introspection?
 это получение информации об объекте во время выполнения. Эта информация может 
 касаться типа объекта, его атрибутов данных и методов, его иерархии наследования 
 классов, документации, сигнатуры метода и т. д.

###########################################################

28. Разница между is и ==? # ===(JS - строгое сравнение) "1" == 1 | "1" === 1

i1 = 12
print(type(i1))


class Mother:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return True

    pass


f1 = Mother(12)  # 1573977310800
f2 = f1  # 1573977310800
f3 = Mother(12)  # 1573977310736

print(id(f1))
print(id(f2))
print(id(f3))
print(f1 is f2)
print(f1 == f2)
print(f1 is f3)
print(f1 == f3)

###########################################################

29. Разница между __init __ () и __new __ ()?
- магические методы
init - инициализатор для создания "сырой сущности", без преднастроек
new - конструктор для воссоздания каких-то преднастроек для класса

class Father:
    def __new__(cls, *args, **kwargs):  # class
        instance = super().__new__(cls)
        # В этом месте можно настроить свой экземпляр класса
        return instance

    def __init__(self, val):
        self.val = val

    def calculate(self):
        self.val *= 2

f1 = Father(12)  # __new__
f1.calculate()
print(f1.val)

###########################################################

30. В чем разница между потоками и процессами?

- процессы - тяжеловесны(дорого и долго)
- потоки внутри процессов

- потоки - threading
- процессы - multiprocessing

- лучше всего async, только затем threading, multiprocessing

###########################################################

31. Какие есть виды импорта?
from main import def1
import main
import main as main2  # alias
from main import *  # !collisions

###########################################################

32. Что такое класс, итератор, генератор?

- представление объекта
- объект, по которому можно пройти циклом
- объект, который может генерировать последовательность, при этом "помнит" только 
текущее значение. __next__()

###########################################################

33. Что такое метакласс, переменная цикла?
for i in range
- это переменная, которая "хранит" текущее значение итератора

for i in range(1, 100):
    pass
print(i)

for i in range(1, 100):
    pass
print(i)

###########################################################

34. В чем разница между итераторами и генераторами?
- yeld(помнит только текущее значение, __next__() - генерирует следующее)
- Exception - вызывает в конце интератора или генератора

###########################################################

35. В чем разница между staticmethod и classmethod?
- staticmethod - первая переменная в классе, больше не является ссылкой(self) | JS: this

- classmethod (cls)

class Figure:
    a1 = 12
    b2 = 13

    @classmethod
    def get_per(cls):
        f4 = cls()  # Figure
        return f4.get_perimeter()

    def get_perimeter(self):
        return (self.a1 + self.b2) * 2

    # @staticmethod
    def get_perimeter2(a2, b2):
        return (a2 + b2) * 2

print(Figure.get_perimeter2(2, 3))

###########################################################

36. Как работают декораторы, контекстные менеджеры?

- декораторы - изменять функцию, не вмешиваясь в неё - аргументы на входе и/или результат на выходе


def decor_twice(func):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        kwargs["c1"] = kwargs["c1"] / 2
        result = func(*args, **kwargs)
        return result
    return wrapper

def decor_round(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return round(result, 2)
    return wrapper

@decor_round
@decor_twice
def sum1(a1, b1, c1):
    return a1 + b1 / c1

print(sum1(1, 2, c1=3))

- контекстные менеджеры (with)

file1 = open('data.txt', 'r')
file1.readlines()
file1.close()

with open('data.txt', 'r') as f:
    f.readlines()

# сначала идёт открытие файла, передача ссылки в 'f'. После выхода из контекстного менеджера идёт "закрытие файла"

class ResourceForWith:
    def __init__(self, name):
        self.__resource = Resource(name)

    def __enter__(self):
        # можно выполнить какие действия до работы с объектом
        return self.__resource

    def __exit__(self, type, value, traceback):
        try:
            # file1.close()
            # можно выполнить какие действия после работы с объектом
            self.__resource.post_work()
        except:
            file1.close()
            pass


###########################################################

37. Как работают dict comprehension, list comprehension и set comprehension?
- list comprehension - синтаксический сахар - сокращение и оптимизация кода, ! не злоупотреблять
list1 = []
for i in range(1, 100+1):
    if i % 2 == 0:
        new_dict = {"id": i}
        list.append(new_dict)
print(list1)

list2 = [{"id": i} for i in range(1, 100+1) if i % 2 == 0]
list2 = (i for i in range(1, 100+1))
list2 = {i: i*2 for i in range(1, 100+1)}

###########################################################

38. Можно ли использовать несколько декораторов для одной функции?

@decor_round
@decor_twice
def sum1(a1, b1, c1):
    return a1 + b1 / c1

###########################################################

39. Можно ли создать декоратор из класса?
- ???

###########################################################

40. Какие есть основные популярные пакеты (requests, pytest, etc)?

- opencv - машинное зрение
- pandas - мат. аппарат для выгрузки(табличные данные)
- numpy - скорость языка C в Python
- requests - веб. Aiohttp
- pytest - QA - автоматизация тестирования vs Manual

###########################################################

41. Что такое lambda-функции?

- lambda-функции - анонимная одноразовая функция

list2 = [{"id": i} for i in range(1, 100+1)]
def check(i):
    return i["id"] % 2 == 0
list3 = filter(check, list2)
list3 = filter(lamdba i: i["id"] % 2 == 0, list2)

###########################################################

42. Что означает *args, **kwargs и как они используются?

- args - принятое название позиционных () аргументов
- kwargs - принятое название именных {} аргументов

* - распаковка(unpacking)

dict1 = {"name": "Bogdan"}

def1(**dict1)
def1(name="Bogdan")

###########################################################

43. Что такое exceptions, <try-except>?

- исключения, для "поимки" ошибок в Runtime. Код может "падать", т.е. дальше не выполняться.

###########################################################

44. Что такое PEP (Python Enhancement Proposal), какие из них знаете (PEP 8, PEP 484)?

- условно принятые соглашения
https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html#section-23

###########################################################

45. Напишите hello-world сервис, используя один из фреймворков.


###########################################################

46. Какие есть типы данных и какая разница между list и tuple, зачем они?
- изменяемость, свойства

###########################################################

47. Как использовать встроенные коллекции (list, set, dictionary)?

list1 = [1, 2, 3, 1]
set1 = set(list1)

###########################################################

48. В чем заключается сложность доступа к элементам dict?
- нужно знать ключ

dict1 = {"name": "Python"}
print(dict1["name1"])  # unsafe
print(dict1.get("name1", "Rubi"))  # safe with default value

###########################################################

49. Как создается объект в Python, для чего __new__, зачем __init__?

###########################################################

50. Что знаете из модуля collections, какими еще built-in модулями пользовались?
OrderedDict, Counter, Decimal
- OrderedDict - хранит порядок элементов
- Counter() - "счётчик", если значения ещё нет, то значение == 0
- Decimal - мне не хватило стандартых 16 знаков, использовал Decimal

dict1 = {"a": 1}  # b == undefined
for i in range:...

dict2 = Counter({"a": 0, "b": 0, "c": 0...})

###########################################################

51. Что такое шаблонизатор и как в нем выполнять базовые операции (объединять участки шаблона, выводить дату, выводить данные с серверной стороны)?
-- ?+

###########################################################

52. Как Python работает с HTTP-сервером?
-- ?+

###########################################################

53. Что происходит, когда создается виртуальная среда?
- в папку "env/venv" устанавливается локальная версия Python
- при этом все библиотеки при активации и установке, "падают" внутрь этой папки

###########################################################

f1 = 12
f2 = 13
f3 = f2
...
# запуск GC(сборщика мусора), он попытается очистить f2
...
print(f1)
print(f3)

###########################################################

What is Python?

- скриптовый язык программирования, изначально задумывался просто для скриптов
- общего назначения(vs 1C), т.е. на нём можно разрабатывать всё
- мультипарадигмальный (Haskell - функциональный / Pascal - процедурный) + ООП

###########################################################

What are the key features of Python?

###########################################################

What are the applications of Python?

###########################################################

What are the global and local variables in Python?

###########################################################

What are the two major loop statements?

- for (итерируемый)  # | foreach | forof | map()
- while (с предусловием)

list1 = []
for i in range(1, 100):
    list1.append(i)

list1 = []
i = 0
while i < 100+1:
    i = i + 1
    list1.append(i)

###########################################################

What are the built-in types available in Python?

###########################################################

speed: cmath|math|numpy|cpython|python+rust

What is the difference between .py and .pyc files?
- .pyc - JIT - динамическая компиляция, бинарный КОД
- .py - 

###########################################################

What do you understand by the term namespace in Python?

###########################################################

What is a boolean in Python?

###########################################################

What are the functions in Python?

###########################################################

What are Python Decorators?

###########################################################

"""
import random

# def func1(list1: list=None):  # для мутабельных(изменяемых) объектов, нельзя задавать стандартное значение
#     if list1 is None:
#         list1 = []
#     list1.append(1)
#     print(list1)

# func1()
# func1()
# func1()


# list2 = [1, 2, 3]
# tuple1 = (1, list2, 3)
# print(tuple1)
# try:
#     tuple1[1] = [3, 3, 3]
# except:
#     pass
# print(tuple1)

# data = (["tuple"], "str")
# try:
#     data[0] += ["list"]
# except:  # неожиданное поведение!
#     print(data)
#
# abs()  # built-in
#
# def abs():  # global
#     pass
#
# def sum1():
#     def abs(): # local
#         pass
#     abs()

"""

Что такое TDD (Test-Driven Development) и как оно применяется в разработке на Python?                        
- придумали идею
- описание её формально, т.е. ТЗ
- реализовали её
- 2-3x loop
- написание автотестов
- запустили в ПРОД

- придумали идею
- описание её формально, т.е. ТЗ
- написание автотестов
- 1-2x loop
- реализовали её
- запустили в ПРОД

class User:
    pass

def register_user(user: User):
    #...
    #...
    return True

def test_register_user(user: User):
    def setUp():
        user = User(name=...)
        register_user(user)
    
    def test():
        connection = ... # просто берём из базы данных пользователя
    #...
    #...
    return True

  

"""

"""
Что такое рекурсия, и какие могут быть проблемы при использовании рекурсивных функций в Python? 

Функция, которая вызывает саму себя.
# единственный способ проходить по объектам в ФП(функциональное программирование)
# 

"""

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def computed(self):
#         return f"{self.name}_{self.age}"
#
# l1 = [User(1), User(2), ...]
#
#
# def computed(i):
#     return f"{i['name']}_{i['age']}"
# l2 = [{"name": 1, "age": 2}, {"name": 1, "age": 2}, ...]

# MVP - minimal varable product

# filter - фильтрация
# range - генератор диапазонов
# map() - вызывает на каждом элементе массива выбранную функцию, возвращает массив результатов
from functools import lru_cache

# size = 3
# 3 3 4 4 3 5 
# FIFO
# LIFO
# lru - least recently used - частота имеет значение

# у вас сервер на ubuntu, оперативы хватает на 10
# home, pricing, pricing 1, .. pricing 9

if __name__ == '__main__':
    class Father:
        def __new__(cls, *args, **kwargs):  # class
            # конструктор - обычно стандартный
            print("Вызван __new__")
            instance = super().__new__(cls)

            rand1 = random.randint(0, 1)
            if rand1:
                return 2

            # В этом месте можно настроить свой экземпляр класса
            return instance

        def __init__(self, val):
            # инициализатор
            print("Вызван __init__")
            self.val = val

        def calculate(self):
            print("Вызван calculate")
            self.val *= 2


    f1 = Father(12)  # __new__ -> __init__
    f1.calculate()
    print(f1.val)
