########################################################################################################################
# TODO декораторы
import datetime
import re
import time


# нужно изменить функцию (значения на входе/выходе, или действия внутри)
# 1 мы не разработчики - нет доступа
# 2 этого функционала ещё нет
# 3 мы не понимаем, как правильно изменить функцию
# 4 таких функций много

def decorator_clear(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper


# декоратор для округления результата до 3 знака после запятой
def decorator_rounding(func):  # определение декоратора -> ссылку на функцию
    def wrapper(*args, **kwargs):  # args - позиционный, key-args - именные
        # todo ДО ФУНКЦИИ
        # ...
        # todo ДО ФУНКЦИИ
        result = func(*args, **kwargs)
        # todo ПОСЛЕ ФУНКЦИИ
        result = round(result, 3)
        # print("data: ", result)
        # todo ПОСЛЕ ФУНКЦИИ
        return result

    return wrapper


def decorator_twise(func):
    def wrapper(*args, **kwargs):
        # todo "ПОДМЕНИЛ" "на лету" первый аргумент входящий в функцию
        print(args, kwargs)
        kwargs["value1"] = kwargs["value1"] * 2
        # args = list(args)
        # print(args)
        # args[0] = args[0] * 2

        result = func(*args, **kwargs)
        return result

    return wrapper


def decorator_time_measure(func):
    def wrapper(*args, **kwargs):
        time_start = time.perf_counter()

        result = func(*args, **kwargs)

        print("elapsed_time(s): ", round(time.perf_counter() - time_start, 6))
        return result

    return wrapper


@decorator_time_measure
@decorator_rounding
def summing(value1, value2, value3):
    res = value1 + value2 + value3
    time.sleep(0.1)  # Ядро функции 1
    return res


@decorator_time_measure
@decorator_twise
# @decorator_rounding
def divider(value1, value2):
    res = value1 / value2
    time.sleep(0.1)  # Ядро функции 1
    return res


#             kwargs       kwargs         kwargs
print(summing(value1=-12, value2=17.0006, value3=1))

#             args  args
print(divider(value1=12, value2=-17))


@decorator_time_measure
def function_something_write(value: int):
    time.sleep(0.15)  # Ядро функции 1
    list1 = [x for x in range(1, 100)]
    sum1 = 0
    for i in list1:
        sum1 += i
    return sum1 + value


print(function_something_write(12))

print("\n\n\n\n\n***********\n\n\n\n")


def validate_user_credentials(function: callable) -> callable:
    def worker(*args, **kwargs):

        if re.match(r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,}$", string=str(args[0])) is None:
            raise Exception("Email not valid")

        if re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{12,}$", string=str(args[1])) is None:
            return False

        res = function(*args, **kwargs)
        return res

    return worker


@validate_user_credentials
def login(email: str, password: str) -> bool:
    # обращение к базе данных
    if email == "admin@gmail.com" and password == "Qwerty!12345":
        return True
    return False


@validate_user_credentials
def register(email: str, password: str, surname) -> bool:
    # запись в базу данных
    if email == "admin@gmail.com" and password == "Qwerty!12345":
        surname += ""
        return True
    return False


# print(login("admin@gmail.com", "Qwerty!123451"))
# print(login("admingmail.com", "Qwerty!12345"))


# У нас есть 3 функции, любые, у них есть аргументы (2-3 аргумента)
# Задача - реализовать декоратор логирования - время обращения, полученные аргументы, результат


print("\n\n\n\n\n***********\n\n\n\n")


def logger(func):
    def wrap(*args, **kwargs):
        func_name = func.__name__
        start = time.perf_counter()
        dat = datetime.datetime.now()

        res = func(*args, **kwargs)
        stop = time.perf_counter()
        elapsed = round(stop - start, 5)

        with open("log.txt", "a", encoding="utf-8") as file:
            text = f"{dat}| {func_name} [{elapsed}] = {res}\n"
            file.write(text)

        return res

    return wrap


@logger
def sum1(val1, val2):
    time.sleep(0.2)
    return val1 + val2


@logger
def sum2(val1, val2):
    return val1 + val2 * 2


@logger
def sum3(val1, val2):
    return val1 + val2 * 3


print(sum1(12, 13))
print(sum2(12, 13))
print(sum3(12, 13))


def template(func):
    def wrap(*args, **kwargs):
        res = func(*args, **kwargs)
        return res

    return wrap


########################################################################################################################

########################################################################################################################
# TODO *args & **kwargs

# args - позиционные аргументы (tuple - кортеж)
# kwargs - именные аргументы (dict - словарь)

def twice_of_divider2(function):
    def wrapper(*args, **kwargs):
        print(args, type(args))  # func2(2, 2) => (2, 2) <class 'tuple'>
        print(args, type(args))  # func2(val1=2, divider=2) => () <class 'tuple'>

        print(kwargs, type(kwargs))  # func2(2, 2) => {} <class 'dict'>
        print(kwargs, type(kwargs))  # func2(val1=2, divider=2) => {'val1': 2, 'divider': 2} <class 'dict'>

        # kwargs["divider"] = kwargs["divider"] * 2
        kwargs["divider"] *= 2

        result = function(*args, **kwargs)

        return result

    return wrapper


@twice_of_divider2
def func2(val1, divider):
    result = val1 / divider
    return result


result2 = func2(2, divider=2)
print(result2)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
tuple1 = (1, 2, 3)
tuple2 = tuple1
# tuple2 = (666, tuple2)
tuple2 = (666, *tuple2[1:])

# list1 = [1, 2, 3, 4]
# print(list1[2:])

# tuple2[0] = 666
print("tuple: ", tuple2)

dict1 = {"name": "Python", "age": 25}


list3 = [*list1, *list2]
# list3.extend(list1)
print(list3)  # [1, 2, 3, 4, 5, 6]
print(*list3)
print(*dict1)

print(dict1.items())
for k, v in dict1.items():
    print(f"{k}  {v}")
