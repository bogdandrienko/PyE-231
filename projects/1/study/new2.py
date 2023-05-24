def sum_arr_danila(start, stop):
    """
    Функция для сложения всех чисел в диапазоне

    :param start: Начало массива для сложения
    :param stop: Окончание массива для сложения(включительно)
    :return: Сумма чисел
    """
    result = 0
    for i in range(start, stop + 1):
        result += i
    # print(result)  # отладка (проверка на работоспособность)
    return result


# res = sum_arr(1, 4)
# print(res)
