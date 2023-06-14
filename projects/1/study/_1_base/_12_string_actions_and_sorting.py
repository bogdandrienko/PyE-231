########################################################################################################################
# TODO поиск

import base64
import chardet

#        0  1  2     3         4               5                   6
list1 = [1, 2, 5, [3, 2, 6], {"key_1": 1}, {1, 2, 3, 5, 7, "123"}, 5]
tuple1 = (1, 2, 5, [3, 2, 6], {"key_1": 1}, {1, 2, 3, 5, 7, "123"}, 5)
str1 = "Banana"

search1 = list1.index(5)  # поиск индекса элемента
print(search1, " : ", list1[search1])

# while True:
#     results_indexes = []
#     target = 5
#     start = 0
#     sr = list1.index(target, __start=start)
#     if sr > -1:
#         results_indexes.append(sr)
#         start = target + 1

search2 = str1.index('a')
print(search2, " : ", str1[search2])

search3 = list1.index(5, 3, 7)  # поиск индекса в массиве по элементу, с указанием откуда и до куда искать
print(search3, " : ", list1[search3])

search4 = tuple1.index(5, 3, 7)
print(search4, " : ", tuple1[search4])

list2 = [1, 2, 5, 10, 4, 2]
list2.sort(reverse=True)  # вызывается на массиве, ничего не возвращает
print(list2)
print(sorted(list2, reverse=False))  # принимает массив как аргумент, возвращает отсортированный

#       01
str1 = "Award"
print(str1.index("a"))
print("".join(sorted(str1)))

char1 = ord("A")  # получаем индекс(число) строчного элемента
print(char1)
print(type(char1))

number1 = chr(35)  # получаем элемент(символ) из индекса
print(number1)
print(type(number1))

text1 = 'Идейные соображения высшего порядка, а также сложившаяся структура организации представляет собой интересный' \
        ' эксперимент проверки форм развития. '

substring = 'форм'
find1 = text1.find(substring)  # start
lenght = find1 + len(substring)  # stop
print(find1)

print(text1[find1:lenght:1])

########################################################################################################################

########################################################################################################################
# TODO кодировки


# UTF-32 utf-16 utf-8 win-1251 win-1252 ascii

str1 = b'123BNO'
print(str1)

rList = [1, 2, 3, 4, 5]

arr = bytes(rList)
print(arr)

encod = base64.b64encode("Admin admin".encode())  # b'QWRtaW4gYWRtaW4='
encod = base64.b64encode(b"Admin admin")  # b'QWRtaW4gYWRtaW4='
print(encod)

decode1 = base64.b64decode(encod)
print(decode1.decode())

source = "Р—Р°РєР°Р· Р·РІРѕРЅРєР° 111111 С‚РµС…РЅРёС‡РµСЃРєРѕР№ РѕРЅРєР° РїРѕРґРґРµСЂР¶РєРё"
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

# шифрование -> текст, с ключом -> набор символов, которые можно расшифровать имея алгоритм и ключ
# обратимая

# хэширование
# односторонняя (необратимая)

# все пароли ВСЕГДА хранятся в хэш-е

text = "Qwerty!12345"
print(hashlib.md5(text.encode()).hexdigest())  # 3f0e60bd4b843524b20575805b69ceeb
# todo MD5 - устарел

print(hashlib.sha256("1".encode()).hexdigest())  # 6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b
# todo sha256 - норма

print(hashlib.sha512("1".encode()).hexdigest())  # 4dff4ea340f0a823f15d3f4f01ab62eae0e5da579ccb851f8db9dfe84c58b2b37b89903a740e1ee172da793a6e79d560e5f7f9bd058a12a280433ed6fa46510a
print(hashlib.sha512("1".encode()).hexdigest())  # 4dff4ea340f0a823f15d3f4f01ab62eae0e5da579ccb851f8db9dfe84c58b2b37b89903a740e1ee172da793a6e79d560e5f7f9bd058a12a280433ed6fa46510a
# todo sha512 - излишен

# TODO hash-функция, всегда при одинаковом значении на входе одинаковый хэш
# коллизии
# 4dff4ea340f0a823f15d3f4f01ab62eae0e5da579ccb851f8db9dfe84c58b2b37b89903a740e1ee172da793a6e79d560e5f7f9bd058a12a280433ed6fa46510a
# 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

# hash_object = hashlib.md5("12345".encode())
# hash_object = hashlib.sha256("key1".encode('utf-8'))
# print(hash_object.hexdigest())

# https://blog.skillfactory.ru/glossary/heshirovanie/

########################################################################################################################


