import datetime
import time


def decorator_rounding(function: callable):
    def wrapper(*args, **kwargs):  # проброс аргументов внутрь функции
        # kwargs["a"] = 2 ** 2  # перехват аргументов
        # return False
        res = function(*args, **kwargs)  # вызов функции(под обёрткой)
        return round(res, 1)  # возврат результат

    return wrapper


# замер производительности
def decorator_time_measuring(function):
    def decorator(*args, **kwargs):
        time_start = datetime.datetime.now()  # точка отсчёта
        result = function(*args, **kwargs)
        time_difference = datetime.datetime.now() - time_start  # разница времени
        print(round(time_difference.total_seconds(), 10), "sec")
        return result

    return decorator


@decorator_rounding
def sum1(a, b):
    # ...
    # ...
    # ...
    # ...
    # ...
    # ...
    # ...
    # ...
    # ...
    return a ** b


@decorator_rounding
def div1(a, b):
    return a / b


@decorator_time_measuring
def mul1(a, b):
    time.sleep(1.1)
    return a * b


print(sum1(1.5, 2))
print(div1(1.5, 2))
print(mul1(1.5, 2))
