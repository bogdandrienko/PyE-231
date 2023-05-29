val = "KZ"


def different(need_value, valute):
    balance = 15000.2

    match valute:
        case "KZ":
            balance = balance + (need_value * 1)
        case "EUR":
            balance = balance + (need_value * 500)
        case "USD":
            balance = balance + (need_value * 450)
    balance_ret = round(balance, 3)
    return balance_ret


# res = different(20.0, "USD")
# print(res)

# написать функцию, которая принимает массив имён и “искомое имя”. Возвращает True если имя есть в массиве.


def search_target_name(list_names, target_name):
    return target_name in list_names  # True / False


def search_target_name2(list_names, target_name):
    if target_name in list_names:
        return True
    else:
        return False


def search_target_name3(list_names, target_name):
    for i in list_names:
        if i == target_name:
            return True

    return False


def search_target_name4(list_names, target_name):
    index = 0
    while index < len(list_names):
        if list_names[index] == target_name:
            return True

        index += 1

    return False


result = search_target_name4(
    list_names=["Богдан", "Евгений", "Гузель"],
    target_name="Евгений"
)


# print(result)


def sr(name, list_names):
    if name in list_names:
        return True
    else:
        return False


r = sr(1, [2, 3, 4, 1, 5, 6])
print(r)
