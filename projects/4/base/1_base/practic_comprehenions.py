# новый массив с квадратами значений другого
list1 = [1, 2, 3, 4, 5]
list2 = []
for i in list1:
    if i % 2 == 0:
        result = i ** 2
        list2.append(result)
print(list2)  # [1, 4, 9, 16, 25]

list2 = []
for i in [1, 2, 3, 4, 5]:
    if i % 2 == 0:
        list2.append(i ** 2)
print(list2)  # [1, 4, 9, 16, 25]

# list comprehension
#       (  item )        (  list      )  (  условие   )
list2 = [i ** 2 for i in [1, 2, 3, 4, 5] if i % 2 == 0]
print(list2)


# пример с условием
list7 = ["P", "p", "p", 5, "p", "P", "p"]
list8 = [x ** 2 for x in list7 if isinstance(x, int)]
print(list8)

# пример для генерации массива словарей
list5 = [101, 201, 301, 401, 501]
list6 = []  # [{"1": 101, "2": 201, "3": 301...]
for i in list5:  # 101, 201...
    new_dict = {str(i)[0]: i}
    list6.append(new_dict)
print(list6)  # [{'1': 101}, {'2': 201}, {'3': 301}, {'4': 401}, {'5': 501}]

list7 = [{str(i)[0]: i} for i in list5]
print(list7)  # [{'1': 101}, {'2': 201}, {'3': 301}, {'4': 401}, {'5': 501}]

# TODO tuple comprehension

# новый массив с квадратами значений другого
list1 = [1, 2, 3, 4, 5]
list2 = []
for i in list1:
    list2.append(i ** 2)
tuple1 = tuple(list2)  # кортеж
print(type(tuple1), tuple1)

list2 = [i ** 2 for i in list1]
print(list2, type(list2))  # [1, 4, 9, 16, 25] <class 'list'>
for i in list2:
    print(i)

# простейший пример
tuple2 = (i ** 2 for i in list1)
print(tuple2, type(tuple2))  # <generator object <genexpr> at 0x000001D56B2B8040> <class 'generator'>
for i in tuple2:
    print(i)













########################################################################################################################
# TODO dict comprehension


# пример для генерации словаря из массива
list5 = [101, 201, 301, 401, 501]
dict6 = {}  # {'1': 101, '2': 201, '3': 301, '4': 401, '5': 501}
for i in list5:
    dict6[str(i)[0]] = i
print(dict6)
dict6 = {str(i)[0]: i for i in list5}
print(dict6)









# # новый словарь из пар значений
list10 = [["key_1", 1], ["key_2", 2], ["key_3", 3]]
dict1 = {}
for k, v in list10:
    dict1[k] = v
print(dict1)  # {'key_1': 1, 'key_2': 2, 'key_3': 3}
dict6 = {k: v for k, v in list5}
