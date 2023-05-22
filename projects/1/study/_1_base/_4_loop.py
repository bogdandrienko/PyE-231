########################################################################################################################
# TODO цикл по итераторам for
import datetime

list_val1 = [1, 2, 3, 4, 5, 6]
for i in list_val1:
    # тело цикла
    print(i)
    # тело цикла
# конец цикла
# print("Python")
for j in ["Гузель", "Анастасия", "Евгений"]:
    print(j)

#            start stop step
for i in range(1, 100+1, 1):  # [1, 2, 3... 99, 100]
    print(i)

for i in range(100, 1, -1):  # [100, 99, 98... 2]
    print(i)

print("\n\n\n***********\n\n\n")

res = 0
for i in range(0, 100 + 1, 2):  # 0, 2, 4, 6 ...
    res = res + i

print(res)

res = 1
for i in range(1, 10 + 1, 1):  # 1, 2, 3, 4 ...
    res = res * i

print(res)  # 3 628 800

print("\n\n\n***********\n\n\n")

#             stop
# for j in range(10):

#           start, stop
# for j in range(5, 10):

#          start, stop, step
for j in range(5, 100 + 1, 1):
    if j >= 50:
        break

    if j % 10 == 0:
        continue

    if j % 2 == 0:
        print("Чётное: ", j)
    else:
        print(j)

print("тормоз цикла")

print("\n\n\n***********\n\n\n")

for i in "Python":
    if i == "y":
        continue
    else:
        print(i)

dict1 = {
    "Имя": "Python",
    "key1": "Анастасия",
    "key2": "Наталья",
    "970801351179": "А.Б.Н. 1997....",
    "970801351178": "А.Б.Н. 1997....",
    1: "Hi",
}

# for i in dict1.values():  # 'Python'
# for i in dict1.keys():  # 'Имя'
for i in dict1.items():  # ('Имя', 'Python')
    print(i)

print("\n\n\n***********\n\n\n")

########################################################################################################################

########################################################################################################################
# TODO условный цикл (с предусловием / с постусловием) while / do while

index = 1
while index < 10:
    print(index)
    index = index + 1

res = 0
stop_value = 0  # "счётчик" для проверки условия цикла
while stop_value <= 100:
    res = res + stop_value
    stop_value = stop_value + 1
print(res)

while True:
    val = input("Тебе больше 18? ")
    if int(val) >= 18:
        break

# while True:
#     print("Привет")


# таймер чч:мм:сс -> .EXE
