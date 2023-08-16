from typing import Union


def summing(a, b, c):
    # res = a + b + c
    # print(res)
    # return res
    return a + b + c


res1 = summing(11, 12, 13)
print(res1)


def divide(a, b):
    # res = a + b + c
    # print(res)
    # return res
    return a / b


print(divide(12, 5))
print(divide(b=5, a=12))


def twice(val1, val2=2):  # функция со стандартным параметром (аргументом)
    return val1 ** val2


print(twice(val1=6))
print(twice(val1=6, val2=3))


# def twice2(val1: Union[int, float], val2=2) -> float | int:
def twice2(val1: int | float, val2=2) -> float | int:
    return val1 + val2


print(twice2(val1=6.0))

list1: list[str] = []
list1.append("hello")
list1.append("world")
# list1.append(12)
for i in list1:
    print(i.upper())


class Values:
    def update(self, var: str, var1: any = 0) -> str | None:
        return "123 Евгений " + var


val1 = Values()


def check(val: Values):
    print(val.update("666"))


print(check(val1))

print(any([False, True, False, False]))
print(any([True, False, False, False]))


def get_name(v: dict):
    return v["name"]


def summary(a, b, c):
    return a + b + c


l_summary = lambda a, b, c: a + b + c

get_n = lambda v: v["name"]

dict1 = {"name": "Bogdan1", "age": 26}

print(get_name(dict1))
print(get_n(dict1))

peoples1 = [
    {"name": "Bogdan3", "age": 20},  # dict 20
    {"name": "Bogdan1", "age": 24},  # dict 24
    {"name": "Bogdan1", "age": 22},  # dict 22
]


# peoples2 = [12, 14, 11]
# print(sorted(peoples2, reverse=True))

def by_age(dictionary: dict) -> int:
    return dictionary["age"]


print(sorted(peoples1, key=by_age, reverse=False))
print(sorted(peoples1, key=lambda d: d["age"], reverse=False))

peoples2 = [
    [1, 1, 99, 4],  # tuple
    ("Python", 2, 6),  # list
    [99, 1, 3],  # list
]

# print(sorted(peoples2))
print(sorted(peoples2, key=lambda c: c[-1]))


def factorial_for(num: int) -> int:
    res = 1
    for j in range(1, num + 1):
        res = res * j  # res *= j
    return res


def factorial_rec(num: int) -> int:  # 5
    if num <= 1:
        return 1
    return num * factorial_rec(num - 1)


def sum_for(end: int) -> int:
    res = 0
    for i in range(1, end + 1):
        res = res + i
    return res


def sum_rec(end: int) -> int:
    if end <= 0:
        return 0
    return end + sum_rec(end - 1)


print(f"sum_for (3): ", sum_for(3))  # 1 + 2 + 3 + 4 + 5
print(f"sum_rec (3): ", sum_rec(3))  # 1 + 2 + 3 + 4 + 5

print(f"factorial for(5): {factorial_for(5)}")
print(f"factorial rec(5): {factorial_rec(5)}")

# палиндром - ОНО, Анна, топот
# аннограмма

str1 = "Оно"  # True
str2 = "ОНА"  # False
str3 = "Bogdan"  # False
str4 = "ТопОт"  # False
str5 = "Я ел мясо лося, млея"  # True

# 1. Регистронезависимое |
# 2. Только буквы(пробелы, знаки...)
# 3. Константная память

def is_check_palindrom(word: str) -> bool:
    # src = word.replace(" ", "")
    # src = word.replace(",", "")
    # src = word.replace("?", "")
    # src = word.replace("!", "")
    # source = word.lower()
    # reversed_ = word[::-1].lower()  # Reversed word
    # return source == reversed_

    # word
    # filter(lambda x: x.isalpha(), word) -> class filter
    # list(filter(lambda x: x.isalpha(), word)) -> список
    # "".join(list(filter(lambda x: x.isalpha(), word)))
    # "".join(list(filter(lambda x: x.isalpha(), word))).lower()
    src = "".join(list(filter(lambda x: x.isalpha(), word))).lower()
    return src == src[::-1]  # не константная память!!!


# middle = рекурсия == O(N)
# middle+ = с опережением == O(N^2)
# hard = метод двух указателей == O(N)


def is_check_palindrom_rec(word: str) -> bool:
    # src == src[::-1]

    if len(word) <= 1:
        return True
    # топот
    if word[0] == word[-1]:
        return is_check_palindrom_rec(word[1:-1])  # опо
    else:
        return False


print(str3, is_check_palindrom(str3))
print(str1, is_check_palindrom(str1))
print(str2, is_check_palindrom(str2))
print(str4, is_check_palindrom(str4))
print(str5, is_check_palindrom(str5))


list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def check(x):
#     return x % 2 == 0
#
# filter(check, list4)  # 1. == функция -> True / False

# print(list(filter(lambda x: x % 2 == 0, list4)))






