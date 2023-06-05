########################################################################################################################
# TODO работа с датой и временем

import time as tm
import datetime
from datetime import datetime

# from datetime import datetime
from datetime import time
# from datetime import timezone
from datetime import timedelta

# timestamp - числовое отображение количества секунд от 1970-01-01 00:00:00


import sys

# print(sys.getsizeof("123123123123"))
# print(sys.getsizeof(123123123123))

# текущее время
val1 = datetime.now()  # 2023-06-05 21:22:40.005624 <class 'datetime.datetime'>
print(val1, type(val1))

# ascii vs unicode
str1 = "Python1112222999"
print(ord("P"))
print(ord("p"))
print(ord("1"))
print(ord("2"))

str2 = "Python2"
print(str1 > str2)  #

# форматирование даты и времени
now1 = datetime.now()  # объект типа "дата и время"
now2 = now1.strftime("%A %B %m-%d-%y, %H:%M:%S.%f")  # Monday June 06-05-2023, 21:30:44.497204 <class 'str'>
print(now2, type(now2))

# https://www.programiz.com/python-programming/datetime/strftime
# https://docs-python.ru/standart-library/modul-datetime-python/kody-formatirovanija-strftime-strptime-modulja-datetime/

print(now1.strftime("%d %B"))
print(now1.strftime("%H:%M"))
print(datetime.now().strftime("%m-%d-%y, %H:%M:%S"))

# получение timestamp
val3 = datetime.now()
val4 = datetime.timestamp(val3)  # 1 685 979 319.438071
print(val4)

val5 = datetime.fromtimestamp(1620333104.005, tz=None)  # 2021-05-07 02:31:44.005000
print(val5)

val12 = datetime.fromtimestamp(1685858400, tz=None)
val13 = datetime.fromtimestamp(1686034800, tz=None)

print(val12, type(val12))
print(val13, type(val13))
print(val13 > val12)
print((val13 - val12).total_seconds() // 60 // 60 / 24)

time_difference = datetime.now() + timedelta(hours=1, minutes=12, seconds=50)
print(time_difference)

########################################################################################################################

########################################################################################################################
# TODO time

# "задержки кода"
print("stopped")
# time.sleep(2.5)  # "код" будет ждать заданное количество секунд
print("running")


# замер производительности
def sum1(start_value: int, stop_value: int) -> int:
    sum_value = 0
    for i in range(start_value, stop_value + 1, 1):
        sum_value += i
    return sum_value


point1 = tm.perf_counter()  # 6161.9708401 <class 'float'>
# point1 = time.perf_counter_ns()
# ДО ФУНКЦИИ
res = sum1(1, 100000000)
print(res)  # 5000000050000000
# ПОСЛЕ ФУНКЦИИ
print(round(tm.perf_counter() - point1, 1))  # 3.3775401000002603

########################################################################################################################
