########################################################################################################################
# TODO коллекции и другие типы данных


import datetime
from collections import OrderedDict
from decimal import Decimal


L = [1, "a", "string", 1 + 2]
print(L)
L.append(6)
print(L)
L.pop()
print(L)
print(L[1])


tup = (1, "a", "string", 1 + 2)
print(tup)
print(tup[1])

dec1 = Decimal(12.5)
print(dec1)

ord_dict1 = OrderedDict(name="Bogdan", age=39)
print(ord_dict1)

list1 = [1, 2, 3, 5, 7, "123"]
print(list1)
print(type(list1))

set1 = set(list1)  # несортированный массив с уникальными значениями
set2 = {1, 2, 3, 5, 7, "123"}
print(set1)
print(type(set1))

set1.add(1111111)  # добавление элемента
print(set1)

set1.add(1111111)  # добавление элемента
print(set1)


