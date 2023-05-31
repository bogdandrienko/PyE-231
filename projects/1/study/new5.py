# Практика: написать функцию, которая принимает 3 массива с числами и возвращает их в
# одном массиве, но отсортированным в порядке возврастая по сумме их “начинки”.

def my_sort(a: list[int], b: list[int], c: list[int], is_reversed=False) -> list[list[int]]:
    # todo Попытка отсортировать "внаглую"
    # res = [a, b, c]
    # print(res)
    # res_sort = sorted(res, reverse=True)
    # print(res_sort)

    # todo пример как выглядит
    # [
    # ([3, 6, 9, 666], 684),   x
    # ([4, 2, 1, 2], 9),       x
    # ([7, 1, 1, 4], 13)       x
    # ]

    # todo создание пар (массив - сумма его чисел), затем сортировка по "ключу"
    tuple_res = sorted(
        ((a, sum(a)), (b, sum(b)), (c, sum(c))),
        key=lambda x: x[1], reverse=is_reversed
    )
    print(tuple_res)

    # todo "извлекаем"(пересобираем в новый массив), но не берём сумму
    res = []
    for i in tuple_res:
        res.append(i[0])
    print(res)

    return res


arr1 = [4, 2, 1, 2]  # 9
arr2 = [7, 1, 1, 4]  # 13
arr3 = [3, 6, 9, 666]  # 684
res = my_sort(arr3, arr1, arr2)
print("Ответ: ", res)

# matrix
# [
#     [6, 7, 8],
#     [1, 2, 3],
#     [3, 4, 5]
# ]
