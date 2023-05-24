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
print(round(2.555, 2))
print(int(2.0))
print(type(True))
print(input("Введите: "))
print(abs(-100))
print(len("Привет"))
print(len([1, 2, 3, 4, 5]))

print(any([False, False, False, False]))
print(any([False, True, False, False]))
print(any([True, False, False, False]))

print(all([True, True, True, True]))
print(all([False, True, True, False]))
print(all([False, False, False]))