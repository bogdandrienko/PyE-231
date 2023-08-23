def convert_to_float(function):
    def wrapper(*args, **kwargs):
        print(args, type(args))  # (1, 2) <class 'tuple'>

        print(kwargs, type(kwargs))  # func2(2, 2) => {} <class 'dict'>

        res = float(function(*args, **kwargs))
        return res

    return wrapper


@convert_to_float
def func1(a, b):
    return f"{a}{b}"


res1 = func1(1, 2)  # args
res1 = func1(a=1, b=2)  # kwargs
res1 = func1(1, b=2)  # args+kwargs
print(type(res1), res1)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8]

# print(list1)
# print(*list1)
# print([*list1, *list2])
print(*[1, 2, 3])
print(1, 2, 3)

dict1 = {"name": "Roman", "age": 666}  # unordered
# print(*dict1)


# print(**dict1)  # name="Roman", age=666

def ex1(age, name):  # ...
    print("name", name)
    print("age", age)


# ex1(dict1)
# ex1(age=dict1["age"], name=dict1["name"])
ex1(**dict1)


def res2():
    return 666, 777

c = res2()
print(c)

a, b = res2()  # auto unpacking
print(a, b)


print("$".join(["1", "2", "3"]))
