import math

from django.test import TestCase


# Create your tests here.


def custom_pagination():
    # limit (количество объектов на 1 странице) = 4
    data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    data2 = [
        [1, 2, 3, 4],  # 1 page
        [5, 6, 7, 8],  # 2 page
        [9]  # 3 page
    ]
    data3 = data2[0]  # [1, 2, 3, 4]

    def paginate(objs: list, selected_page: int = 1, limit: int = 4) -> list:
        """Функция, которая разбивает входящий массив на страницы и возращает выбранную страницу"""
        length = len(objs)
        count_page = math.ceil(length / limit)
        print(length, count_page)

        global_arr = []
        local_arr = []
        for obj in objs:
            if len(local_arr) == limit:
                global_arr.append(local_arr)
                local_arr = []
            local_arr.append(obj)
            # print(global_arr, local_arr)
        global_arr.append(local_arr)
        local_arr = []
        # print(global_arr, local_arr)

        return global_arr[selected_page - 1]

    # https://www.youtube.com/watch?app=desktop&v=Pp84Sv041xA&t=18594s&ab_channel=%D0%93%D0%BB%D0%B5%D0%B1%D0%9C%D0%B8%D1%85%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2

    print(paginate([9, 8, 7, 6, 5, 4, 3, 2, 1], 2, 4))
