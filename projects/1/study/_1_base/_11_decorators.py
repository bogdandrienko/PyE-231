########################################################################################################################
# TODO декораторы
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
    list1 = [x for x in range(1, 10000000)]
    sum1 = 0
    for i in list1:
        sum1 += i
    return sum1 + value


print(function_something_write(12))
