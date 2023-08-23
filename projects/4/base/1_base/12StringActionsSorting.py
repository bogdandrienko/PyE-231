########################################################################################################################
# TODO поиск

import base64
import chardet

#        0  1  2     3         4               5                   6
list1 = [1, 2, 5, [3, 2, 6], {"key_1": 1}, {1, 2, 3, 5, 7, "123"}, 5]
tuple1 = (1, 2, 5, [3, 2, 6], {"key_1": 1}, {1, 2, 3, 5, 7, "123"}, 5)
str1 = "Banana"

search1 = list1.index(5)  # поиск индекса в массиве по элементу
print(search1, " : ", list1[search1])
search2 = str1.index('a')
print(search2, " : ", str1[search2])

search3 = list1.index(5, 3, 7)  # поиск индекса в массиве по элементу, с указанием откуда и до куда искать
print(search3, " : ", list1[search3])

search4 = tuple1.index(5, 3, 7)
print(search4, " : ", tuple1[search4])

list2 = [1, 2, 5, 10, 4, 2]
list2.sort()  # изменяет изначальную коллекцию
print(list2)

#       01
str1 = "Award"
print(str1.index("w"))
print("".join(sorted(str1)))
# print("$".join(["1", "2", "3"]))

char1 = ord("A")  # получаем индекс(число) строчного элемента
print(char1)
print(type(char1))

number1 = chr(35)  # получаем элемент(символ) из индекса
print(number1)
print(type(number1))

list5 = [1, 2, 5, 10, 4, 2]
print(list5)
list5.sort(reverse=True)
print(list5)

str1 = "Award"
print(str1)
arr1 = []
for x in str1:
    arr1.append(x)
print(arr1)
arr2 = [x for x in str1]  # list comprehensions
print(arr2)
arr2.sort(reverse=False)
print(arr2)
str3 = ''
for x in arr2:
    str3 += x
print(str3)
# print(str1)
str4 = "".join(arr2)
print(str4)

arr6 = [x for x in "Award"]
arr6.sort(reverse=True)
arr8 = "".join(arr6)
print(arr8)

text1 = 'Идейные соображения высшего порядка, а также сложившаяся структура организации представляет собой интересный' \
        ' эксперимент проверки форм развития. '

substring = 'структура'
find1 = text1.find(substring)
print(find1)
print(text1[find1:find1 + len(substring):1])

########################################################################################################################

########################################################################################################################
# TODO кодировки


# utf-8 win-1251 win-1252 ascii

str1 = b'123BNO'

rList = [1, 2, 3, 4, 5]

arr = bytes(rList)
print(arr)

encod = base64.b64encode("Admin Admin".encode())

print(encod)

decode1 = base64.b64decode(encod)

print(decode1.decode())

source = "Р—Р°РєР°Р· Р·РІРѕРЅРєР° С‚РµС…РЅРёС‡РµСЃРєРѕР№ РїРѕРґРґРµСЂР¶РєРё"
print(f"source: {source}\n")

print(chardet.detect(source.encode())['encoding'])

source1 = source.encode(encoding='cp1251')
print(f"source1: {source1}\n")

source2 = source1.decode(encoding='utf-8')
print(f"source2: {source2}\n")

########################################################################################################################

########################################################################################################################
# TODO хэширование

import hashlib
import uuid

# hash_object = hashlib.md5("12345".encode())
hash_object = hashlib.sha256("key1".encode('utf-8'))
print(hash_object.hexdigest())

########################################################################################################################
