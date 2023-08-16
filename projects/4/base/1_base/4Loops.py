########################################################################################################################
# TODO цикл по итераторам for

list_val1 = [1, 2, 3, 4, 5, 6]
for i in list_val1:  # next()
    print(i)

#        ["P", "y", "t"...]
for j in "Python":
    print(j)

#            start stop step
for i in range(1, 100 + 1, 1):
    print(i)

for i in range(100, 1, -1):  # [100, 99... 2]
    print(i)

for i in range(1, 100, 1):
    print(i)
    for j in "Python":
        print(str(i) + " | " + j)





# сумма всех чётных чисел до 100
sum1 = 0
for i in range(1, 100 + 1, 1):
    if i % 2 == 0:
        # sum1 += i
        sum1 = sum1 + i
    else:
        print("Число нечётное, не добавляем")
print(sum1)






for j in range(1, 5000):
    if j % 2 != 0:
        continue  # пропускает эту итерацию цикла
    if j >= 50:
        break  # останавливает цикл
    print(j)

# проход циклом по словарю
value7 = {
    "key_1": "value_1",
    "key_2": 10,
    "key_3": True
}
for key in value7.keys():
    print(key)
for value in value7.values():
    print(value)
for item in value7.items():
    print(item)
    print(item[0], item[1])
for key, value in value7.items():  # auto unpacking
    print(key, value)

########################################################################################################################

########################################################################################################################
# TODO условный цикл (с предусловием / с постусловием) while / do while

index = 1
while index <= 10:
    print(index)
    index = index + 1

# бесконечный цикл!
# while True:
#     print("Hello")

i = 0
while True:
    i = i + 1
    if i <= 3:
        continue  # пропускает эту итерацию цикла
    elif i >= 7:
        break  # останавливает цикл
    print(i)

########################################################################################################################

########################################################################################################################
# TODO "таймер" с использованием цикла

# импорт библиотеки "time"
import time

hours = 0
minutes = 0
seconds = 0

# таймер
while True:
    # seconds = seconds + 1
    seconds += 1

    if seconds > 59:
        minutes += 1
        seconds = 0

    if minutes > 59:
        hours += 1
        minutes = 0

    if hours > 23:
        seconds = 0
        minutes = 0
        hours = 0

    time.sleep(1.0)
    print(f"{hours}:{minutes}" + ":" + str(seconds))
# код после цикла

########################################################################################################################
