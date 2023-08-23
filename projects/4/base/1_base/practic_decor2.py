# "обёртка" для функции -> изменяет либо результат либо входные параметры

# Нужно реализовать декоратор для трёх функций, который будет конвертировать результат в float


def convert_to_float(function):
    def wrapper(*args, **kwargs):
        try:
            return float(function(*args, **kwargs))
        except Exception as error:
            print(error)
            raise error

    return wrapper


@convert_to_float
def func1(a, b):
    return f"{a}{b}"


@convert_to_float
def func2(a):
    return a ** 2


@convert_to_float
def func3(a):
    return a / 2


res1 = func1(1, 2)
print(type(res1), res1)

res2 = func2(2)
print(type(res2), res2)

res3 = func3(1)
print(type(res3), res3)
