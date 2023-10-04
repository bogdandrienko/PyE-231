def ex1():
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


def ex2():
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


def ex7():
    import queue
    import random
    import zlib
    import time
    from random import randint
    from timeit import repeat
    from collections import deque, defaultdict

    class Task1:
        """
        Вывод пересечений не уникальных элементов из массива

        Условие:
        # Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
        # Надо вернуть [1, 2, 2, 3] (порядок неважен)
        """

        @staticmethod
        def error_brufors(first: list[int], second: list[int]) -> list[int]:  # ошибка: если в первом 2 числа одинаковых,
            # а втором 3, то будет ответ как 3, вместо 2

            result1 = []
            for i in first:
                if i in second:
                    result1.append(i)
            result1.sort()

            return result1

        @staticmethod
        def good_default_dict(first: list[int], second: list[int]) -> list[int]:  # с использованием
            b_dict = defaultdict(int)
            for i in second:
                b_dict[i] += 1

            result1 = []
            for i in first:
                if b_dict[i] > 0:
                    result1.append(i)
                    b_dict[i] -= 1

            return result1

        @staticmethod
        def good_dictionary(first: list[int], second: list[int]) -> list[int]:  # стандартные средства, моё решение
            result1: list[int] = []
            dictionary1: dict[int, int] = {}
            for i in first:
                if dictionary1.get(i, 0) > 0:
                    dictionary1[i] += 1
                else:
                    dictionary1[i] = 1

            for i in second:
                if dictionary1.get(i, 0) > 0:
                    result1.append(i)
                    dictionary1[i] -= 1

            return result1

    class Task2:
        """
        Метод двух указателей

        Условие:
        Дан массив целых чисел, необходимо вернуть индексы двух чисел, сумма которых равна заданному числу. Можно считать,
        что массив будет иметь ровно одно решение. Нельзя использовать одно и то же число дважды.
        """

        @staticmethod
        def bad_brutefors(nums: list[int], target: int) -> list[int]:  # O(n^2)
            for i, _ in enumerate(nums):
                for j, _ in enumerate(nums):
                    if i != j and nums[i] + nums[j] == target:
                        return [i, j]

            raise Exception("the pair must be found")

        @staticmethod
        def good_two_pointers(nums: list[int], target: int) -> list[int]:  # сложность по времени O(n) и по памяти O(1).
            left, right = 0, len(nums) - 1
            while left < right:
                cur_sum = nums[left] + nums[right]

                if cur_sum == target:
                    return [left, right]
                elif target > cur_sum:
                    left += 1
                else:
                    right -= 1

            raise Exception("the pair must be found")

        @staticmethod
        def good_dictionaries(nums: list[int], target: int) -> list[int]:  # сложность по времени O(n) и по памяти O(n).
            m = {}  # храним числа и их индексы

            # заполняем словарь
            for i, x in enumerate(nums):
                m[x] = i

            # ищем парное значение
            for i, x in enumerate(nums):
                complement = target - x

                # если существует парное значение и его индекс не равен текущему
                if complement in m and m[target - x] != i:
                    return [i, m[target - x]]

            raise Exception("the pair must be found")

    class Task3:
        """
        Двоичный, или бинарный, поиск значения

        Условие:
        Нужно проверить, содержит ли массив искомое значение, а также в определение места его нахождения.
        """

        @staticmethod
        def good_iterations(nums: list[int], target: int) -> int:  # итерациями
            low = 0
            mid = len(nums) // 2
            high = len(nums) - 1

            while nums[mid] != target and low <= high:
                if target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
                mid = (low + high) // 2

            if low > high:
                raise Exception("value not found")
            else:
                return mid

        @staticmethod
        def good_recursion(nums: list[int], target: int, start=0, end=-1) -> int:  # рекурсия
            if end == -1:
                end = len(nums)

            if start > end:
                return -1

            mid = (start + end) // 2
            if target == nums[mid]:
                return mid

            if target < nums[mid]:
                return Task3.good_recursion(nums, target, start, mid - 1)
            else:
                return Task3.good_recursion(nums, target, mid + 1, end)

    class Task4:
        """
        Проверка "сбалансированности" строки со скобками

        Условие:
        string1 = '{()}[{}]'        # balanced
        string2 = '{[{}{}]}[()]'    # balanced
        string3 = '{(})'            # not balanced
        """

        @staticmethod
        def is_balanced(string: str):
            if not string or len(string) & 1:
                return False

            open_s = "({["
            closed_s = ")}]"
            stack = []

            for char in string:
                if char in open_s:
                    stack.append(char)  # Если текущий символ является открывающей скобкой поместите его в массив
                if char in closed_s:
                    if not stack:
                        return False  # Если символа нет, то нет баланса
                    top = stack.pop()  # Если текущий символ является закрывающей скобкой извлечь его из массива
                    if (top == '(' and char != ')') or (top == '{' and char != '}' or (top == '[' and char != ']')):
                        return False  # Если символ "зеркально" не совпадает, то нет баланса
            return not stack  # Если массив пустой, то есть баланс

    class Task5:
        """
        Проверка строки на "аннограмму"

        Условие:
        source = "tea"
        word1 = "eat"
        word2 = "toa"
        """

        @staticmethod
        def check(string_source: str, string_example: str) -> bool:
            dict1: dict[str, int] = {}
            for i in string_source:
                if dict1.get(i, None) is None:
                    dict1[i] = 1
                else:
                    dict1[i] += 1

            for i in string_example:
                elem = dict1.get(i, None)
                if elem is None or elem < 1:
                    return False
                else:
                    dict1[i] -= 1
                    if dict1[i] == 0:
                        del dict1[i]
            return dict1 == {}

    class Task6:
        """
        Реализация собственного словаря

        Условие:
        Ключом в ассоциативном массиве может быть абсолютно любая строка. Но здесь есть одно противоречие:
        Все возможные ключи — это бесконечное множество
        В качестве результата хеш-функция выдает строку фиксированной длины, то есть это конечное множество
        Такую ситуацию принято называть коллизией. Простейший способ разрешения коллизий — это открытая адресация.
        Она предполагает последовательное перемещение по слотам хеш-таблицы в поисках первого свободного слота, куда
        значение будет записано.
        """

        # https://ru.hexlet.io/courses/python-dicts/lessons/hash-table/theory_unit
        class HashMap(object):  # HashTable(синхронизированы в потоках)
            def __init__(self):
                # ассоциативный_массив[индекс, ключ(хэшированный), значение]
                self.internal: list[int | any, str | any, any] = []

            def __repr__(self):
                for i in self.internal:
                    print(*i)
                return "\n"

            def setter(self, key_for_dictionary: str, value: any) -> None:
                """
                Добавляет или обновления значение в ассоциативном массиве
                """

                # Любые данные, которые мы хотим хэшировать, представляются в виде байтовой строки
                __hash = zlib.crc32(key_for_dictionary.encode(encoding="utf-8"))

                # Это делается для того, чтобы индексы не были слишком большими. От этого зависит потребление памяти.
                __index = abs(__hash) % 1000

                # Псевдокод, на самом деле поиск занимает в среднем O(1)
                for index, i in enumerate(self.internal, 0):
                    if i[0] == __index:
                        self.internal[index] = [__index, (key_for_dictionary, value)]
                        return
                # Тут происходит добавление в ассоциативный массив
                self.internal.append([__index, (key_for_dictionary, value)])

            def getter(self, key_for_dictionary: str, default=None) -> any:
                """
                Пытается извлечь значение по ключу из ассоциативного массива или стандартное значение, в противном случае
                вызывает ошибку
                """

                # Любые данные, которые мы хотим хэшировать, представляются в виде байтовой строки
                __hash = zlib.crc32(key_for_dictionary.encode("utf-8"))

                # Это делается для того, чтобы индексы не были слишком большими. От этого зависит потребление памяти.
                __index = abs(__hash) % 1000

                # Псевдокод, на самом деле поиск занимает в среднем O(1)
                for i in self.internal:
                    if i[0] == __index:
                        return i[1][1]

                if default is not None:
                    return default
                raise KeyError("Ключа нет в словаре")

        @staticmethod
        def check():
            map1 = Task6.HashMap()
            print(map1)

            map1.setter("name", "Bogdan1")
            print(map1)

            print(map1.getter("name"))

            map1.setter("name1", "Bogdan3")
            map1.setter("name", "Bogdan2")
            print(map1)

    class Task7:
        """
        Реализация LIFO & FIFO

        Условие:
        Алгоритмы - «FIFO» (первый пришел – первый ушел) и «LIFO» (последний пришел – первый ушел)
        """

        class LifoQueueList(object):
            def __init__(self) -> None:
                self.__store: list[int] = []

            def push_default(self, value: int) -> None:
                self.__store.append(value)

            def pop_default(self, index=-1) -> int:
                return self.__store.pop() if index < 0 else self.__store.pop(index)

            def reverse_default(self) -> list[int]:
                self.__store.reverse()
                return self.__store

            def push(self, value: int) -> None:
                self.__store = [*self.__store, value]

            def pop(self, index=-1) -> int:
                if index < 0:
                    value = self.__store[len(self.__store) - 1]
                    del self.__store[len(self.__store) - 1]
                else:
                    value = self.__store[index]
                    del self.__store[index]

                return value

            def reverse(self) -> list[int]:
                # self.__store = list((x for x in self.__store[::-1]))
                self.__store = list((self.__store[len(self.__store) - 1 - x] for x in range(0, len(self.__store) - 1 + 1)))

                return self.__store

        class FifoQueueList(object):
            def __init__(self) -> None:
                self.__store: list[int] = []

            def push(self, value: int) -> None:
                self.__store = [*self.__store, value]

            def pop(self, index=-1) -> int:
                if index < 0:
                    value = self.__store[0]
                    del self.__store[0]
                else:
                    value = self.__store[index]
                    del self.__store[index]

                return value

            def reverse(self) -> list[int]:
                # self.__store = list((x for x in self.__store[::-1]))
                self.__store = list((self.__store[len(self.__store) - 1 - x] for x in range(0, len(self.__store) - 1 + 1)))

                return self.__store

        @staticmethod
        def check():
            q1 = queue.Queue()

            q1.put(11)
            q1.put(5)
            q1.put(4)
            q1.put(10)
            q1.put(21)
            q1.put(3)

            n = q1.qsize()
            for i in range(n):
                x = q1.get()
                for j in range(n - 1):
                    y = q1.get()
                    if x > y:
                        q1.put(y)
                    else:
                        q1.put(x)
                        x = y
                q1.put(x)

            while q1.empty() is False:
                print(q1.queue[0], end=" ")
                q1.get()

            print("------------")

            que1 = Task7.LifoQueueList()

            que1.push_default(666)
            que1.push_default(123)
            que1.push_default(333)
            que1.push_default(222)

            print(que1.pop_default())
            print(que1.pop_default())
            print(que1.reverse_default())
            print(que1.pop_default())
            print(que1.pop_default())

            print("------------")

            que1.push(666)
            que1.push(123)
            que1.push(333)
            que1.push(222)

            print(que1.pop())
            print(que1.pop())
            print(que1.reverse())
            print(que1.pop())
            print(que1.pop())

            print("------------")

            que2 = Task7.FifoQueueList()

            que2.push(666)
            que2.push(123)
            que2.push(333)
            que2.push(222)

            print(que2.pop())
            print(que2.pop())
            print(que2.reverse())
            print(que2.pop())
            print(que2.pop())

            print("------------")

    class Task8:
        @staticmethod
        def time_measure(func: any) -> any:
            def wrapper(*args, **kwargs) -> list[int]:
                t_start = time.perf_counter()
                res = func(*args, **kwargs)
                t_stop = time.perf_counter()
                print('Elapsed time: ', round((t_stop - t_start), 5), " s")
                return res

            return wrapper

        @staticmethod
        @time_measure
        def sort_sorted(_src: list[int], is_reversed=False) -> list[int]:
            return sorted(_src, reverse=is_reversed)

        @staticmethod
        @time_measure
        def sort_quicksort(_src: list[int], is_reversed=False) -> list[int]:
            def start_quicksort(__src: list[int], _is_reversed=False) -> list[int]:
                length = len(__src)
                if length < 2:
                    return __src
                low, same, high = [], [], []
                pivot = __src[randint(0, length - 1)]
                for item in __src:
                    if _is_reversed:
                        if item > pivot:
                            low.append(item)
                        elif item == pivot:
                            same.append(item)
                        elif item < pivot:
                            high.append(item)
                    else:
                        if item < pivot:
                            low.append(item)
                        elif item == pivot:
                            same.append(item)
                        elif item > pivot:
                            high.append(item)
                return start_quicksort(low, is_reversed) + same + start_quicksort(high, is_reversed)

            return start_quicksort(_src, is_reversed)

        @staticmethod
        @time_measure
        def sort_insertion(_src: list[int], is_reversed=False) -> list[int]:
            length = len(_src)
            for i in range(1, length):
                key_item = _src[i]
                j = i - 1
                if is_reversed:
                    while j >= 0 and _src[j] < key_item:
                        _src[j + 1] = _src[j]
                        j -= 1
                else:
                    while j >= 0 and _src[j] > key_item:
                        _src[j + 1] = _src[j]
                        j -= 1
                _src[j + 1] = key_item

            return _src

        @staticmethod
        @time_measure
        def sort_bubble(_src: list[int], is_reversed=False) -> list[int]:
            length = len(_src)
            for i in range(length - 1):
                already_sorted = True
                for j in range(length - i - 1):
                    if is_reversed:
                        if _src[j] < _src[j + 1]:
                            _src[j], _src[j + 1] = _src[j + 1], _src[j]
                            already_sorted = False
                    else:
                        if _src[j] > _src[j + 1]:
                            _src[j], _src[j + 1] = _src[j + 1], _src[j]
                            already_sorted = False
                if already_sorted:
                    break
            return _src

        @staticmethod
        @time_measure
        def sort_merge(_src: list[int], is_reversed=False) -> list[int]:
            def start_merge(__src: list[int], _is_reversed=False) -> list[int]:
                def merge(left, right):
                    if len(left) == 0:
                        return right
                    if len(right) == 0:
                        return left
                    result = []
                    index_left = index_right = 0
                    if _is_reversed:
                        while len(result) < len(left) + len(right):
                            if left[index_left] >= right[index_right]:
                                result.append(left[index_left])
                                index_left += 1
                            else:
                                result.append(right[index_right])
                                index_right += 1
                            if index_right == len(right):
                                result += left[index_left:]
                                break
                            if index_left == len(left):
                                result += right[index_right:]
                                break
                    else:
                        while len(result) < len(left) + len(right):
                            if left[index_left] <= right[index_right]:
                                result.append(left[index_left])
                                index_left += 1
                            else:
                                result.append(right[index_right])
                                index_right += 1
                            if index_right == len(right):
                                result += left[index_left:]
                                break
                            if index_left == len(left):
                                result += right[index_right:]
                                break

                    return result

                if len(__src) < 2:
                    return __src
                midpoint = len(__src) // 2
                return merge(
                    left=start_merge(__src[:midpoint], _is_reversed),
                    right=start_merge(__src[midpoint:], _is_reversed)
                )

            return start_merge(__src=_src, _is_reversed=is_reversed)

        @staticmethod
        def run_sorting_algorithm(algorithm, array):
            times = repeat(
                setup=f"from __main__ import {algorithm}" if algorithm != "sorted" else "",
                stmt=f"{algorithm}({array})",
                repeat=3,
                number=10
            )
            print(f"Algorithm: {algorithm}. Execution time: {times}")

        @staticmethod
        def check():
            # source1 = [5, 2, 6, 111, 7, 8, 12, 15]
            source1 = [randint(0, 1000) for _ in range(1000)]
            _is_reversed = True
            # run_sorting_algorithm(algorithm="sort_bubble", array=array)

            print("Original list:\n", source1, '\n')
            print("Default sort:\n", Task8.sort_sorted(source1, _is_reversed), '\n')
            print("Quicksort sort:\n", Task8.sort_quicksort(source1, is_reversed=_is_reversed), '\n')
            print("Insertion sort:\n", Task8.sort_insertion(source1, is_reversed=_is_reversed), '\n')
            print("Bubble sort:\n", Task8.sort_bubble(source1, is_reversed=_is_reversed), '\n')
            print("Merging sort:\n", Task8.sort_merge(source1, is_reversed=_is_reversed), '\n')

    class Task9:
        # Структура данных для хранения узла бинарного дерева
        class Node:
            def __init__(self, data, left=None, right=None):
                self.data = data
                self.left = left
                self.right = right

        # Функция для проверки, является ли данный токен оператором
        @staticmethod
        def is_operator(c):
            return c == '+' or c == '-' or c == '*' or c == '/' or c == '^'

        # Напечатать постфиксное выражение для дерева выражения
        @staticmethod
        def postorder(root):
            if root is None:
                return
            Task9.postorder(root.left)
            Task9.postorder(root.right)
            print(root.data, end='')

        # Распечатать инфиксное выражение для дерева выражений
        @staticmethod
        def inorder(root):
            if root is None:
                return

            # если текущий токен является оператором, вывести открывающую скобку
            if Task9.is_operator(root.data):
                print('(', end='')

            Task9.inorder(root.left)
            print(root.data, end='')
            Task9.inorder(root.right)

            # если текущий токен является оператором, вывести закрывающую скобку
            if Task9.is_operator(root.data):
                print(')', end='')

        # Функция построения дерева выражения из заданного постфиксного выражения.
        @staticmethod
        def construct(postfix):
            # Базовый вариант
            if not postfix:
                return

            # создает пустой stack для хранения указателей дерева
            s = deque()

            # пересекает постфиксное выражение
            for c in postfix:
                # если текущий токен является оператором
                if Task9.is_operator(c):
                    # извлекает из stack два узла `x` и `y`
                    x = s.pop()
                    y = s.pop()

                    # построить новое бинарное дерево, корнем которого является оператор, а
                    # левый и правый дочерние элементы указывают на `y` и `x` соответственно.
                    node = Task9.Node(c, y, x)

                    # помещает текущий узел в stack
                    s.append(node)

                # если текущий токен является операндом, создать новый узел бинарного дерева
                # корень которого является операндом, и поместите его в stack
                else:
                    s.append(Task9.Node(c))

            # указатель на корень дерева выражений остается в stack
            return s[-1]

        @staticmethod
        def check():
            postfix = 'ab+cde+**'
            root = Task9.construct(postfix)

            print('Postfix Expression: ', end='')
            Task9.postorder(root)

            print('\nInfix Expression: ', end='')
            Task9.inorder(root)

    class Task10:
        class BinaryTreeInstance:
            def __init__(self, data: int):
                self.data: int = data
                self.right: Task10.BinaryTreeInstance | None = None
                self.left: Task10.BinaryTreeInstance | None = None

            def __repr__(self):
                lines, *_ = self.__display()
                for line in lines:
                    print(line)
                return '\n'

            def insert(self, data: int) -> None:
                if self.data <= data:
                    if self.right is None:
                        self.right = Task10.BinaryTreeInstance(data)
                    else:
                        self.right.insert(data)
                elif self.data > data:
                    if self.left is None:
                        self.left = Task10.BinaryTreeInstance(data)
                    else:
                        self.left.insert(data)

            def __display(self):
                line = f"{self.data}"
                width = len(line)

                # todo none child
                if self.right is None and self.left is None:
                    return [line], width, 1, width // 2

                # todo right child
                if self.left is None:
                    lines, n, p, x = self.right.__display()
                    return [line + x * '_' + (n - x) * ' ', (width + x) * ' ' + '\\' + (n - x - 1) * ' '] + \
                           [width * ' ' + line for line in lines], n + width, p + 2, width // 2

                # todo left child
                if self.right is None:
                    lines, n, p, x = self.left.__display()
                    return [(x + 1) * ' ' + (n - x - 1) * '_' + line, x * ' ' + '/' + (n - x - 1 + width) * ' '] + \
                           [line + width * ' ' for line in lines], n + width, p + 2, n + width // 2

                # todo both child
                if self.right is not None and self.left is not None:
                    left, n, p, x = self.left.__display()
                    right, m, q, y = self.right.__display()
                    if p < q:
                        left += [n * ' '] * (q - p)
                    elif q < p:
                        right += [m * ' '] * (p - q)
                    return [
                               (x + 1) * ' ' + (n - x - 1) * '_' + line + y * '_' + (m - y) * ' ',
                               x * ' ' + '/' + (n - x - 1 + width + y) * ' ' + '\\' + (m - y - 1) * ' '
                           ] + [a + width * ' ' + b for a, b in zip(left, right)], n + m + width, max(p,
                                                                                                      q) + 2, n + width // 2

        class BinaryTreeInstance2:
            def __init__(self, key=0):
                self.key: int = key
                self.left: Task10.BinaryTreeInstance2 | None = None
                self.right: Task10.BinaryTreeInstance2 | None = None

            def __str__(self):
                self.print_hierarchy()
                return "\n"

            def insert(self, key):
                if self.key is None:
                    self.key = key
                    return
                if key < self.key:
                    if self.left is None:
                        self.left = Task10.BinaryTreeInstance2(key)
                    else:
                        self.left.insert(key)
                elif key > self.key:
                    if self.right is None:
                        self.right = Task10.BinaryTreeInstance2(key)
                    else:
                        self.right.insert(key)
                else:
                    raise KeyError(f"Key {key} already exists")

            def print_hierarchy(self, _dir="root", level=0):
                print(f"[{_dir}] #{level} = {self.key} | "
                      f"left = {f'TreeNode({self.left.key})' if self.left else None} | "
                      f"right = {f'TreeNode({self.right.key})' if self.right else None} | ")
                if self.left is not None:
                    self.left.print_hierarchy("left", level + 1)
                if self.right is not None:
                    self.right.print_hierarchy("right", level + 1)
                return ""

        class RBTreeInstance:
            class RBNodeInstance:
                def __init__(self, val):
                    self.red = False
                    self.parent = None
                    self.val = val
                    self.left = None
                    self.right = None

            def __init__(self, data: int):
                self.nil = Task10.RBTreeInstance.RBNodeInstance(data)
                self.nil.red = False
                self.nil.left = None
                self.nil.right = None
                self.root = self.nil

            def __repr__(self):
                lines = []
                Task10.RBTreeInstance.print_tree(self.root, lines)
                return '\n'.join(lines)

            @staticmethod
            def print_tree(node, lines, level=0):
                if node.val != 0:
                    Task10.RBTreeInstance.print_tree(node.left, lines, level + 1)
                    lines.append('-' * 4 * level + '> ' + str(node.val) + ' ' + ('r' if node.red else 'b'))
                    Task10.RBTreeInstance.print_tree(node.right, lines, level + 1)

            def insert(self, val):
                new_node = Task10.RBTreeInstance.RBNodeInstance(val)
                new_node.parent = None
                new_node.left = self.nil
                new_node.right = self.nil
                new_node.red = True

                parent = None
                current = self.root
                while current != self.nil:
                    parent = current
                    if new_node.val < current.val:
                        current = current.left
                    elif new_node.val > current.val:
                        current = current.right
                    else:
                        return

                new_node.parent = parent
                if parent is None:
                    self.root = new_node
                elif new_node.val < parent.val:
                    parent.left = new_node
                else:
                    parent.right = new_node

                self.fix_insert(new_node)

            def fix_insert(self, new_node):
                while new_node != self.root and new_node.parent.red:
                    if new_node.parent == new_node.parent.parent.right:
                        u = new_node.parent.parent.left
                        if u.red:
                            u.red = False
                            new_node.parent.red = False
                            new_node.parent.parent.red = True
                            new_node = new_node.parent.parent
                        else:
                            if new_node == new_node.parent.left:
                                new_node = new_node.parent
                                self.rotate_right(new_node)
                            new_node.parent.red = False
                            new_node.parent.parent.red = True
                            self.rotate_left(new_node.parent.parent)
                    else:
                        u = new_node.parent.parent.right

                        if u.red:
                            u.red = False
                            new_node.parent.red = False
                            new_node.parent.parent.red = True
                            new_node = new_node.parent.parent
                        else:
                            if new_node == new_node.parent.right:
                                new_node = new_node.parent
                                self.rotate_left(new_node)
                            new_node.parent.red = False
                            new_node.parent.parent.red = True
                            self.rotate_right(new_node.parent.parent)
                self.root.red = False

            def exists(self, val):
                curr = self.root
                while curr != self.nil and val != curr.val:
                    if val < curr.val:
                        curr = curr.left
                    else:
                        curr = curr.right
                return curr

            def rotate_left(self, x):
                y = x.right
                x.right = y.left
                if y.left != self.nil:
                    y.left.parent = x

                y.parent = x.parent
                if x.parent is None:
                    self.root = y
                elif x == x.parent.left:
                    x.parent.left = y
                else:
                    x.parent.right = y
                y.left = x
                x.parent = y

            def rotate_right(self, x):
                y = x.left
                x.left = y.right
                if y.right != self.nil:
                    y.right.parent = x

                y.parent = x.parent
                if x.parent is None:
                    self.root = y
                elif x == x.parent.right:
                    x.parent.right = y
                else:
                    x.parent.left = y
                y.right = x
                x.parent = y

        @staticmethod
        def check():
            # todo BinaryTreeInstance
            tree1 = Task10.BinaryTreeInstance(0)
            for i in range(1, 50 + 1):
                # tree1.insert(i)
                tree1.insert(random.randint(0, 100))
            print(tree1)

            print("\n----------\n")

            # todo BinaryTreeInstance2
            tree2 = Task10.BinaryTreeInstance2()
            tree2.insert(9)
            tree2.insert(17)
            tree2.insert(4)
            print(tree2)
            print("\n")

            tree2.insert(3)
            tree2.insert(100)
            tree2.insert(6)
            print(tree2)
            # tree.insert(3)  # exception

            print("\n----------\n")

            # todo RBTreeInstance
            tree = Task10.RBTreeInstance(0)
            for x in range(1, 51):
                tree.insert(x)
            print(tree)

    if __name__ == "__main__":
        # todo Вывод пересечений не уникальных элементов из массива
        # source1_1 = [1, 2, 3, 2, 0]
        # source1_2 = [5, 1, 2, 7, 3, 2]
        # print(Task1.error_brufors(source1_1, source1_2))
        # print(Task1.good_default_dict(source1_1, source1_2))
        # print(Task1.good_dictionary(source1_1, source1_2))

        # todo Метод двух указателей
        # source2 = [2, 7, 11, 15]
        # elem2 = 9
        # print(Task2.bad_brutefors(source2, elem2))
        # print(Task2.good_two_pointers(source2, elem2))
        # print(Task2.good_dictionaries(source2, elem2))

        # todo Бинарный поиск
        # source3 = [7, 15, 15, 17, 18, 25, 27, 31, 33, 39]
        # print(Task3.good_iterations(source3, 31))
        # print(Task3.good_recursion(source3, 31))

        # todo Баланс скобок в строке
        # source4_1 = '{[{}{}]}[()]'
        # source4_2 = '{(})'
        # print('balanced' if Task4.is_balanced(string=source4_1) else 'not balanced')
        # print('balanced' if Task4.is_balanced(string=source4_2) else 'not balanced')

        # todo Проверка строки на аннограмму
        # source5_1 = "tea"
        # source5_2 = "eat"
        # source5_3 = "toa"
        # print(Task5.check(source5_1, source5_2))
        # print(Task5.check(source5_1, source5_3))

        # todo Реализация собственного словаря
        # Task6.check()

        # todo Реализация LIFO & FIFO
        # Task7.check()

        # todo Реализация сортировок
        # Task8.check()

        # todo Реализация сортировок
        # Task8.check()

        # todo Реализация бинарного дерева
        # Task9.check()

        # todo Реализация бинарных деревьев
        # Task10.check()

        pass

