########################################################################################################################
# TODO условный оператор if-else

bool_condition1 = False

if 10 > 5:
    # todo если условие соблюдается
    print("Правда 1")
# else:
#     pass

if bool_condition1:
    # todo если условие соблюдается
    print("Правда 2")
else:
    # todo если условие не соблюдается
    print("Ложь 2")
    print("привет Данила")

value = 40

if value > 100:
    print("Правда 3 1")
else:
    if value > 50:
        print("Правда 3 2")
    else:
        if value > 30:
            print("Правда 3 3")
        else:
            if value > 20:
                print("Правда 3 4")
            else:
                print("Ложь 3 1")
# выход
print("1111")

if value > 100:
    print("Правда 3 1")
elif value > 50:
    print("Правда 3 2")
elif value > 30:
    print("Правда 3 3")
elif value > 20:
    print("Правда 3 4")
else:
    print("Ложь 3 1")
# выход

fruit = "абрикос"
if fruit == "абрикос":
    print("У Вас аллергия, будьте осторожны")

elif fruit == "банан":
    print("Всё в норме")

elif fruit == "яблоко":
    print("очень полезно")

else:
    print("Неизвестный фрукт")

# таблица истинности
# https://ru.wikipedia.org/wiki/%D0%A2%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0_%D0%B8%D1%81%D1%82%D0%B8%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D0%B8
cond1 = 12 <= 5
cond2 = 12 == 12
cond3 = 12 < 7
if (cond1 and cond2) or cond3:
    print("Правда 4")
else:
    print("Ложь 4")

# [] - False, [''] - True, '' - False, 1 - True, 0 - False
l1 = ''
if l1:
    print("l1")
else:
    print('l2')

########################################################################################################################

########################################################################################################################
# TODO условный оператор match-case (+ python 3.10)

light = "Зелёный"
match light:
    case "Красный":
        print("Стоять")
    case "Жёлтый":
        print("Готовьтесь")
    case "Зелёный":
        print("Можно идти")
    case _:
        print("Светофор сломался")

fruit = "абрикос"
match fruit:
    case "абрикос":
        print("У Вас аллергия, будьте осторожны")
    case "банан":
        print("Всё в норме")
    case "яблоко":
        print("Всё в норме")
    case _:
        print("Неизвестный фрукт")

########################################################################################################################

########################################################################################################################
# TODO тернарный оператор

a = 10
b = 20

res = ''
if a > b:
    res = 'Больше'
else:
    res = 'Меньше'

res2 = 'Больше' if a > b else 'Меньше'

res3 = a if a < b else b

print(res)
print(res2)
print(res3)

########################################################################################################################
