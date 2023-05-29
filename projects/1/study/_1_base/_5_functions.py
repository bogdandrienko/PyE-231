########################################################################################################################
# TODO функции


# print("Hi")
# print("Hi 1")
# print("Hi")
# print("Hi 1")
# print("Hi")

# DRY - don't repeat yourself
# def - define - определить

# todo код "до" функции
def hi():  # todo определение функции
    # todo код "внутри" функции (отступы: 4 пробела)
    print("Hi")


# todo код "после" функции


# hi()  # вызов функции
# hi()  # вызов функции


# грязная функция
def twice_value1(val1, val2):  # функция с параметрами (аргументами)
    result = val1 + val2
    print(result)


# twice_value1(12, 13)
# twice_value1(3, 5)
# twice_value1(90, 10)


def sum1(v):
    print(v)
    print("я закончила свою работу")


def sum2(v):
    print(v)
    return v ** 2


res1 = sum1(4)  # Попытка присвоить результат из функции
print(res1)  # None == внутри функции нет 'return'
res2 = sum2(4)  # Попытка присвоить результат из функции
print(res2)  # 16


# print(sum1())
# print(sum2())


# чистая функция
def twice_value2(val1, val2):
    result = val1 ** val2
    return result  # возврат значения


res1 = twice_value2(25, 2)  # позиционные аргументы
print(res1)
result2 = twice_value2(val2=2, val1=6)  # именные аргументы
print(result2)


def sqrt_v2(val1, val2=2, val3=1):  # функция со стандартным параметром (аргументом)
    """
    docstring

    Функция
    :param val1: исходное число, которое будет возводиться в квадрат
    :param val2: степень для числа
    :param val3: делитель после степени
    :return: возврат результата всех действий
    """

    # todo 50 строчек кода
    return (val1 ** val2) // val3


print(sqrt_v2(4, 3))  # 16
print(sqrt_v2(5))  # 16
print(sqrt_v2(6, val3=2))  # 16
print(help(sqrt_v2))


def empty():
    """
    Пустая функция, на будущее
    :return:
    """
    pass


print(help(empty))

print("\n\n\n\n\n\n***********\n\n\n\n\n\n")


########################################################################################################################

########################################################################################################################
# TODO типизация

# Типизация - строгое задание типов для переменных и параметров (аргументов)
# Python (СPython) - динамическая сильная типизация (+ скорость разработки - скорость работы + к багам)
# JavaScript - динамическая слабая типизация (+ скорость разработки - скорость работы  + к багам)
# C++ - статическая типизация (- скорость разработки + скорость работы - к багам)
# C# - статическая типизация (- скорость разработки + скорость работы - к багам)


def divide(val1: int, val2: float) -> int | float:
    # word = "Python"
    # char1 = word[val2]

    result = val1 / val2
    return result


res = divide(10, 2)
print(res / 2)
print("Перечислить деньги на карту")

list_numbers: list[int] = [1, 2, 3]

for i in list_numbers:
    print(i // 2)

########################################################################################################################

########################################################################################################################
# TODO стандартные функции

print(sum([1, 2, 3]))


def sum1(list_args: list[int | float]) -> int | float:
    res29 = 0.0
    for i9 in list_args:
        res29 += i9
    return res29


print(sum([1, 3, 5.0]))
print(sum1([1, 3, 5]))

print(round(2.555, 2))
print(int(2.0))
print(type(True))
# print(input("Введите: "))
print(abs(-100))


def abs1(val):
    if val < 0:
        return val * -1
    else:
        return val


print(abs(10), abs(-666))
print(abs1(10), abs1(-666))

print(len("Привет"))  # 6


def len1(word: str):
    index = 0
    for i in word:
        index += 1
    return index


print(len([1, 2, 3, 4, 5]))

print(any([False, False, False, False]))  # False
print(any([False, True, False, False]))  # True
print(any([True, False, False, False]))  # True

print(all([True, True, True, True]))  # True
print(all([False, True, True, False]))  # False
print(all([False, False, False]))  # False
elems = [1, 12, 2, 9, 8]
print(elems)
print(sorted(elems))
print(sorted(elems, reverse=True))

# ...
# https://pythonru.com/osnovy/vstroennye-funkcii-python
# https://letpy.com/handbook/builtins/


print("\n\n\n\n\n\n***********\n\n\n\n\n\n")


########################################################################################################################

########################################################################################################################
# TODO анонимные функции (lambda)

def multi(a, b):
    return a * b


multi2 = lambda a, b: a * b

a = lambda a: a ** 2

print(multi(7, 8))
print(multi2(7, 8))
print(a(9))

peoples1 = [
    {"name": "Bogdan1", "age": 22},  # dict 22
    {"name": "Bogdan2", "age": 30},  # dict 30
    {"name": "Bogdan1", "age": 24},  # dict 24
    {"name": "Bogdan3", "age": 20},  # dict 20
]
# print(sorted(peoples1))

pep1 = {"name": "Bogdan1", "age": 27.2}


def get_age(dict1):
    return dict1["age"]


print(get_age(pep1))
print(sorted(peoples1, key=get_age, reverse=True))
print(sorted(peoples1, key=lambda x: x["name"], reverse=False))


def div1(a, b):
    return a / b


div2 = lambda a, b: (a / b) ** 2

peoples2 = [
    [1, 1, 99, 4],  # list
    ("Python", 2, 6),  # tuple
    [99, 1, 3],  # list
]

print(sorted(peoples2, key=lambda x: x[-1], reverse=True))

print("\n\n\n\n\n\n***********\n\n\n\n\n\n")


########################################################################################################################

########################################################################################################################
# TODO рекурсивные функции (рекурсия)

# процедурный (код - портянка сверху вниз, справа налево)
# ООП - объектно-ориентированный (сущности-объекты и взаимодействие между ними - Ячейка, Строки, Колонки, Рабочий Лист, Рабочая книга)
# Функциональный - (очень математический - нет циклом(рекурсия), нет грязных функций ), Haskell)


def while_counter(value_from):
    # while value_from > 0:
    #     print(value_from)  # 10 9 8 7 6 5 4 3 2 1
    #     value_from -= 1
    # print("конец")

    for i in range(value_from, 0, -1):
        print(i)
    print("конец")


while_counter(10)


def recursion_counter(value_from):
    print(value_from)
    if value_from <= 1:
        return 1
    else:
        recursion_counter(value_from - 1)


recursion_counter(10)


def recursion_factorial(n):
    if n <= 1:
        return 1
    return n * recursion_factorial(n - 1)


def while_factorial(n):
    counter = 1
    while n > 0:
        counter *= n  # 1 * 4  *   1 * 3  *  1 * 2  *  1 * 1
        n -= 1
    return counter


print(recursion_factorial(4))
print(while_factorial(4))


def recursion_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursion_sum(n - 1)


def while_sum(n):  # 5 | 0 + 1 + 2 + 3 + 4 + 5
    result = 0
    while n > 0:
        result = result + n
        n -= 1
    return result


print(recursion_sum(100))
print(while_sum(100))

str5 = "мадам"
tr6 = "лёшанаполкеклопанашёл"
tr7 = "8777 ".strip()


def is_palindrome1(text: str) -> bool:
    # a = text
    # b = text[::-1]
    # print(a, b)
    # print(a == b)
    # return text == text[::-1]
    return text.replace(" ", "").lower() == text[::-1].replace(" ", "").lower()


def is_palindrome2(text: str) -> bool:  # "мадам"
    if len(text) < 1:
        return True
    elif text[0] == text[-1]:
        return is_palindrome2(text[1:-1])
    else:
        return False


print(is_palindrome1("мадам"))
print(is_palindrome2("мадам"))

print("\n\n\n\n\n\n***********\n\n\n\n\n\n")
########################################################################################################################

########################################################################################################################
# TODO области видимости

res2 = "Привет"  # глобальная область видимости
print(res2)  # "Привет"

def sym1():
    res2 = "Пока"  # локальная область видимости func1
    print(res2)  # "Пока"


def sym2():
    global res2  # использование переменной из глобальной области видимости
    res2 = "Пока"  # локальная область видимости func1
    print(res2)


# print(res2)
# sym1()
# print(res2)

# Привет
# Пока
# Привет

print(res2)
sym2()
print(res2)

# Привет
# Пока
# Пока

# пример сложнее
local_var = 12  # глобальная область видимости (scope)
print(local_var)


def func1(a):
    # global local_var  # использование переменной из глобальной области видимости
    # print(local_var)
    local_var = 10  # локальная область видимости func1
    print(local_var)
    print(a)  # 12

    def func2(b):
        # global local_var  # использование переменной из глобальной области видимости
        # print(local_var)

        local_var = 8  # локальная область видимости func2
        print(local_var)

        print("b:", b)

    func2(a)


func1(local_var)
