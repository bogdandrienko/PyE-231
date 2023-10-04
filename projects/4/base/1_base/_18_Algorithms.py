"""
https://proglib.io/p/slozhnost-algoritmov-i-operaciy-na-primere-python-2020-11-03
"Сложность алгоритмов и операций на примере Python.html"

«O» большое служит обозначением временной сложности операций алгоритма. Она показывает, сколько времени потребуется
алгоритму для вычисления требуемой операции.
На письме временная сложность алгоритма обозначается как O(n), где n — размер входной коллекции.

O(1)
Обозначение константной временной сложности. Независимо от размера коллекции, время, необходимое для выполнения
операции, константно.

O(log n)
Обозначение логарифмической временной сложности. В этом случае когда размер коллекции увеличивается, время,
необходимое для выполнения операции, логарифмически увеличивается.

O(n)
Обозначение линейной временной сложности. Время, необходимое для выполнения операции, прямо и линейно пропорционально
количеству элементов в коллекции.

O(n log n)
Обозначение квазилинейной временной сложности. Скорость выполнения операции является квазилинейной функцией числа
элементов в коллекции.

O(n^2)
Обозначение квадратичной временной сложности. Время, необходимое для выполнения операции, пропорционально квадрату
элементов в коллекции.

O(n!)
Обозначение факториальной временной сложности. Каждая операция требует вычисления всех перестановок коллекции,
следовательно, требуемое время выполнения операции является факториалом размера входной коллекции.
"""

"""
Благоприятные, средние и худшие случаи
При вычислении временной сложности операции можно получить сложность на основе благоприятного, среднего или худшего 
случая.

Благоприятный случай. Как следует из названия, это сценарий, когда структуры данных и элементы в коллекции вместе с 
параметрами находятся в оптимальном состоянии. Например, мы хотим найти элемент в коллекции. Если этот элемент 
оказывается первым элементом коллекции, то это лучший сценарий для операции.

Средний случай. Определяем сложность на основе распределения значений входных данных.

Худший случай. Структуры данных и элементы в коллекции вместе с параметрами находятся в наиболее неоптимальном 
состоянии. Например, худший случай для операции, которой требуется найти элемент в большой коллекции в виде списка — 
когда искомый элемент находится в самом конце, а алгоритм перебирает коллекцию с самого начала.
"""

"""
Коллекции Python и их временная сложность - 

* Список (list):
Вставка: O(n).
Получение элемента: O(1).
Удаление элемента: O(n).
Проход: O(n).
Получение длины: O(1)

* Множество (set)
Проверить наличие элемента в множестве: O(1).
Отличие множества A от B: O(длина A).
Пересечение множеств A и B: O(минимальная длина A или B).
Объединение множеств A и B: O(N) , где N это длина (A) + длина (B).

* Словарь (dict)
Получение элемента: O(1).
Установка элемента: O(1).
Удаление элемента: O(1).
Проход по словарю: O(n).
"""

"""



"""

########################################################################################################################
# TODO сортировка пузырьком

numbers_orig = [5, 2, 6, 7, 8, 12, 15, 111]


def myBubbleSort(myList):
    for i in range(len(myList) - 1):
        for j in range(len(myList) - i - 1):
            if myList[j] < myList[j + 1]:
                temp = myList[j]
                myList[j] = myList[j + 1]
                myList[j + 1] = temp


print("Original list:")
print(numbers_orig)
myBubbleSort(numbers_orig)
print("Sorted list:")
print(numbers_orig)


########################################################################################################################

########################################################################################################################
# TODO бинарное дерево


class BinaryTree:
    def __init__(self, data: int):
        self.left = None
        self.right = None
        self.root = data

    def get_data(self):
        return self.root

    def insert_new_data(self, data: int):
        if self.root:
            if data < self.root:
                # левый
                if self.left is not None:
                    self.left.insert_new_data(data)
                else:
                    self.left = BinaryTree(data)
                # левый

            elif data > self.root:
                # правый
                if self.right is not None:
                    self.right.insert_new_data(data)
                else:
                    self.right = BinaryTree(data)
                # правый

            else:
                print("Значение повторяется")

        else:
            self.root = data

    def print_all_edges(self):
        print(self.root)
        print(self.left)
        print(self.right)


tree1 = BinaryTree(1)  # создание экземляра класса - создание объекта
tree1.insert_new_data(2)
tree1.insert_new_data(3)
tree1.insert_new_data(9)
tree1.insert_new_data(6)
tree1.insert_new_data(11)
tree1.insert_new_data(15)
print(f"root: {tree1.root}")
print(f"root: {tree1.right.root}")

print(f"root: {tree1.right.right.root}")

print(f"root: {tree1.right.right.right.root}")

print(f"root: {tree1.right.right.right.right.root}")
print(f"root: {tree1.right.right.right.left.root}")

print(f"root: {tree1.right.right.right.right.right.root}")

########################################################################################################################

########################################################################################################################
# TODO шифр Цезаря


class CaesarCipher(object):
    """
    Цезарь шифрование и дешифрование
    """

    def __crypt(self, char, key):
        """
        Зашифровать одну букву, смещение
        @param char: {str} один символ
        @param key: {num} смещение
        @return: {str} зашифрованный символ
        """
        if not char.isalpha():
            return char
        else:
            base = "A" if char.isupper() else "a"
            return chr((ord(char) - ord(base) + key) % 26 + ord(base))

    def encrypt(self, char, key):
        """
        Шифровать персонажей
        """
        return self.__crypt(char, key)

    def decrypt(self, char, key):
        """
        Расшифровать символы
        """
        return self.__crypt(char, -key)

    def __crypt_text(self, func, text, key):
        """
        Зашифровать текст
        @param char: {str} текст
        @param key: {num} смещение
        @return: {str} зашифрованный текст
        """
        lines = []
        for line in text.split("\n"):
            words = []
            for word in line.split(" "):
                chars = []
                for char in word:
                    chars.append(func(char, key))
                words.append("".join(chars))
            lines.append(" ".join(words))
        return "\n".join(lines)

    def encrypt_text(self, text, key):
        """
        Зашифровать текст
        """
        return self.__crypt_text(self.encrypt, text, key)

    def decrypt_text(self, text, key):
        """
        Расшифровать текст
        """
        return self.__crypt_text(self.decrypt, text, key)


plain = """
you know? I love you!
"""
key = 3

cipher = CaesarCipher()

# Шифрование
print(cipher.encrypt_text(plain, key))
# brx nqrz? L oryh brx!

# Расшифровать
print(cipher.decrypt_text("brx nqrz? L oryh brx!", key))


# you know? I love you!

########################################################################################################################

def ex1():
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

def ex3():
    import random
    import sys
    import time

    # import memory_profiler
    # mprof run --include-children python bad_optimizing.py
    # mprof plot --output bas_optimizing.png

    # pip install memory_profiler
    # pip install matplotlib

    # @memory_profiler.profile
    def start():
        cars = []  # todo СТРУКТУРА ДАННЫХ "ЛИСТ" вся хранится в оперативной памяти!
        for i in range(1, car_count + 1):
            new_car = {"id": i, "name": random.choice(car_names), "color": random.choice(car_colors)}
            cars.append(new_car)
        # for j in cars:
        #     print(j)

        # 24 * 60 * 60
        # ~ 100 000
        # 3 000 000 * 500
        # 150 000 000
        print(round(sys.getsizeof(cars) / 1024 / 1024, 1), "megabytes")
        return cars

    if __name__ == "__main__":
        time_start = time.perf_counter()

        car_names = ["Toyota", "Honda", "Audi", "Nissan"]
        car_colors = ["Black", "Blue", "Red", "Yellow", "White"]
        car_count = 50000000

        # сборщик мусора (GC) - замедляет работу кода, но упрощает работу работу с паматью
        # (Python, PHP, JavaScript, Java, Go, C#) vs (C++, Rust, C, Assembler)

        cars_arr = start()
        with open("bad.txt", "w", encoding="utf-8") as file:
            for car in cars_arr:
                file.write(f'{car["id"]} | {car["name"]} |{car["color"]}\n')

        print(round(sys.getsizeof(cars_arr), 1), "bytes")
        print(round(time.perf_counter() - time_start, 3), "s elapsed time")


def ex4():
    import random
    import sys
    import time

    # import memory_profiler
    # mprof run --include-children python good_optimizing.py
    # mprof plot --output good_optimizing.png

    def start():
        for i in range(1, car_count + 1):
            new_car = {"id": i, "name": random.choice(car_names), "color": random.choice(car_colors)}
            yield new_car

    if __name__ == "__main__":
        time_start = time.perf_counter()

        car_names = ["Toyota", "Honda", "Audi", "Nissan"]
        car_colors = ["Black", "Blue", "Red", "Yellow", "White"]
        car_count = 50000000  # 232

        # сборщик мусора (GC) - замедляет работу кода, но упрощает работу работу с паматью
        # (Python, PHP, JavaScript, Java, Go, C#) vs (C++, Rust, C, Assembler)

        # @memory_profiler.profile
        def start2():
            cars_arr = start()
            with open("good.txt", "w", encoding="utf-8") as file:
                for car in cars_arr:
                    file.write(f'{car["id"]} | {car["name"]} |{car["color"]}\n')

            print(round(sys.getsizeof(cars_arr), 1), "bytes")
            print(round(time.perf_counter() - time_start, 3), "s elapsed time")

        start2()

def ex5():
    # 1. Алгоритмы встречаются чаще на высоких нагрузках
    # кэш, позволяет ускорить получение данных от 100 до 100000
    import random
    import time

    # 3 s = 1(10 000 * 0.01s) s + 1(10 000 * 0.01s) s + 1(10 000 * 0.01s) s
    # 300
    # 3 s = 1 * 0.01s(10 000 * 0.0001s) s + 1(10 000 * 0.01s) s + 1(10 000 * 0.01s) s
    # 3.03

    # list1 = [1, 2, 3, 4, 5, 6, ...]  #... 100
    # for i in list1:  # линейное
    #     time.sleep(0.01)  # 1.0
    #     print(i)
    #
    # for i in list1:
    #     for j in list1:  # квадратичная
    #         time.sleep(0.01)  # 10000
    #         print(j)
    # for j in list1:  # кубическая
    #     time.sleep(0.01)  # 1 000 000
    #     print(i)

    # 3 s = 1(1 * 0.01s + 10 000 * 0.0001) s + 1(10 000 * 0.01s) s + 1(10 000 * 0.01s) s
    # 3.03

    # кэш | ssd | шардирование | репликация | рейд-массив

    # -> получить новость -> идёт обращение на api (0.05s) -> идёт обработка провайдером (0.01s) ->
    # -> идёт проверка прав (0.02s) -> накладные расходы web (fastapi django) (0.05s) -> обращение в базу данных (0.2s) ->
    # -> сериализация данных (.py) (0.07s) -> возврат
    # -> сериализация данных (.rs) (0.002s)

    # https://medium.com/@MatthieuL49/a-mixed-rust-python-project-24491e2af424
    # https://dudochkin-victor.github.io/blog/speed-up-your-python-using-rust/

    # leetcode  https://www.youtube.com/watch?v=Pp84Sv041xA&t=18594s&ab_channel=%D0%93%D0%BB%D0%B5%D0%B1%D0%9C%D0%B8%D1%85%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2
    # codewars

    # hash / binary / binary tree / palindrome
    #

    list1 = [x for x in range(1, 10 + 1)]
    list2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # print(list1)
    time_start = time.perf_counter()

    def extract(data):
        time.sleep(0.01)
        return

    # for i in list1:  # линейное 0.107
    #     extract(i)
    #     print(i)

    # for j in list2:
    #     for i in list1:  # квадратичная  2.806
    #         extract(j)
    #         print(f"{i}_{j}")

    # N = 100

    # set() | dict()
    # O(1) = 1s - константное время выполнения
    # O(logN) = 10s - линейное время выполнения
    # O(N) = 100s - линейное время выполнения
    # O(N*2) = 200s - 2x линейное время выполнения
    # O(NlogN) = 1000s - линейное время выполнения
    # O(N^2) = 10000s - квадратичное время выполнения
    # O(N!2) = s - ...

    # преждевременная оптимизация
    # рефакторинг

    # print("Заняло времени: ", round(time.perf_counter() - time_start, 3))

    # Сортировка    l.sort()    O(N Log N)

    # https://proglib.io/p/slozhnost-algoritmov-i-operaciy-na-primere-python-2020-11-03
    # https://machinelearningmastery.ru/understanding-time-complexity-with-python-examples-2bda6e8158a7/
    # https://habr.com/ru/companies/kts/articles/727528/

    # https://www.youtube.com/watch?v=Pp84Sv041xA&t=18594s&ab_channel=%D0%93%D0%BB%D0%B5%D0%B1%D0%9C%D0%B8%D1%85%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2

    # бинарное дерево - (красные/чк деревья)

    #
    # обычный поиск, для 240 000 элементов, где 1 шаг стоит 1s, в худшем случае 240 000s
    # бинарный поиск, для 240 000 элементов, где 1 шаг стоит 1s, в худшем случае 18s
    #

    def time_measure(func):
        def wrapper(*args, **kwargs):
            time_start = time.perf_counter()
            res = func(*args, **kwargs)
            time_end = time.perf_counter()
            print(round(time_end - time_start, 10))
            return res

        return wrapper

    @time_measure
    def default_sort(source: list[int]):
        return sorted(source)

    @time_measure
    def bubble_sort(source: list[int]):
        new_source = source
        length = len(new_source)
        for i in range(1, length):
            for j in range(0, length - i):
                if new_source[j] > new_source[j + 1]:
                    # temp = data[j]  # временное хранилище для пузырька
                    # data[j] = data[j+1]
                    # data[j+1] = temp
                    new_source[j], new_source[j + 1] = new_source[j + 1], new_source[j]  # поменяли местами
        return new_source

    @time_measure
    def selection_sort(arr: list[int]):
        for i in range(1, len(arr)):
            minimum = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[minimum]:
                    minimum = j
            arr[minimum], arr[i] = arr[i], arr[minimum]  # поменяли местами
        return arr

    @time_measure
    def insertion_sort(source):
        for cur_idx in range(1, len(source)):
            prev_idx = cur_idx - 1
            val = source[cur_idx]
            while prev_idx > 0 and source[prev_idx] > val:
                source[prev_idx + 1] = source[prev_idx]
                prev_idx -= 1
            source[prev_idx + 1] = val
        return source

    class BinaryTree:
        def __init__(self, data: int):
            self.left = None
            self.right = None
            self.root = data

        def get_data(self):
            return self.root

        def insert_new_data(self, data: int):
            if self.root:
                if data < self.root:

                    # левый
                    if self.left is not None:
                        self.left.insert_new_data(data)
                    else:
                        self.left = BinaryTree(data)
                    # левый

                elif data > self.root:

                    # правый
                    if self.right is not None:
                        self.right.insert_new_data(data)
                    else:
                        self.right = BinaryTree(data)
                    # правый

                else:
                    print('Значение повторяется')

            else:
                self.root = data

        def print_all_edges(self):
            print(self.root)
            print(self.left)
            print(self.right)

    if __name__ == "__main__":
        list1 = [113, 236, 729, 204, 91, 582, 379, 876, 496, 393, 852, 757, 980, 41, 998, 720, 200, 851, 361, 110, 148, 46,
                 990, 45, 480, 319, 479, 826, 882, 68, 749, 120, 304, 52, 466, 325, 61, 73, 792, 421, 350, 620, 983, 70,
                 772, 374, 922, 74, 602, 441, 69, 237, 616, 299, 674, 301, 305, 887, 261, 181, 162, 377, 47, 65, 503, 710,
                 889, 184, 128, 46, 592, 679, 534, 952, 447, 37, 791, 30, 219, 972, 925, 466, 835, 962, 17, 487, 510, 504,
                 325, 532, 834, 94, 780, 670, 629, 264, 859, 360, 843, 931] * 50
        # print(list1)
        # print(default_sort(list1))      # 0.0002551
        # print(bubble_sort(list1))       # 0.9373299
        # print(selection_sort(list1))    # 0.3777373
        # print(insertion_sort(list1))    # 0.0004259
        # merge sort

        # tree1 = BinaryTree(1)  # создание экземляра класса - создание объекта
        # tree1.insert_new_data(2)
        # tree1.insert_new_data(3)
        # tree1.insert_new_data(9)
        # tree1.insert_new_data(6)
        # tree1.insert_new_data(11)
        # tree1.insert_new_data(15)
        # print(f"root: {tree1.root}")
        # print(f"root: {tree1.right.root}")
        # print(f"root: {tree1.right.right.root}")
        # print(f"root: {tree1.right.right.right.root}")
        # print(f"root: {tree1.right.right.right.right.root}")
        # print(f"root: {tree1.right.right.right.left.root}")
        # print(f"root: {tree1.right.right.right.right.right.root}")

    class Task7:
        """
        Реализация LIFO & FIFO

        Условие:
        Алгоритмы - «FIFO» (первый пришел – первый ушел) и «LIFO» (последний пришел – первый ушел)
        """

    class Task4:
        """
        Проверка "сбалансированности" строки со скобками

        Условие:
        string1 = '{()}[{}]'        # balanced
        string2 = '{[{}{}]}[()]'    # balanced
        string3 = '{(})'            # not balanced
        """

    class Task5:
        """
        Проверка строки на "аннограмму"

        Условие:
        source = "tea"
        word1 = "eat"
        word2 = "toa"
        """

    class Tree:
        def __init__(self, val: int):
            self.root = val
            self.left = None
            self.right = None

    tr1 = Tree(8)
    tr2 = Tree(3)
    tr3 = Tree(6)
    tr4 = Tree(1)

    tr2.left = tr4
    tr2.right = tr3
    tr1.left = tr2

    print(tr1)  # <__main__.Tree object at 0x000002235F33F290>
    print(tr1.root)  # 8 tr1.root
    print(tr1.left.root)  # 3 tr2.root
    print(tr1.right)  # None

    print(tr1.left.right.root)  # 6
    print(tr1.left.left.root)  # 1

    class Tree2:
        def __init__(self, val: int):
            self.root = val
            self.right = None
            self.left = None

        def __repr__(self):
            lines, *_ = self.__display()
            for line in lines:
                print(line)
            return '\n'

        def insert(self, data: int) -> None:
            if data >= self.root:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Tree2(data)
            else:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Tree2(data)

        def __display(self):
            line = f"{self.root}"
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

    # todo BinaryTreeInstance
    # tree1 = Tree2(0)
    # for i in range(1, 50 + 1):
    # tree1.insert(i)
    # tree1.insert(random.randint(0, 100))
    # print(tree1)

    tree1 = Tree2(8)
    tree1.insert(3)
    tree1.insert(10)
    tree1.insert(1)
    tree1.insert(6)
    tree1.insert(11)
    tree1.insert(4)
    tree1.insert(7)
    tree1.insert(11)
    tree1.insert(5)

    print(tree1)

    s = input()
    stack = []
    is_good = True
    if is_good and len(stack) == 0:
        print("balanced")
    else:
        print("not balanced")


def ex6():
    import random
    import time

    def sort_sorted(_source: list[int], _reverse=False) -> list[int]:
        # _source.sort(reverse=_reverse)  # сортирует прям этот массив, но ничего не возвращает
        new_sorted_array = sorted(_source, reverse=_reverse)  # сортирует и возвращает отсортированный массив
        return new_sorted_array

    def sort_bubble(_src: list[int], _reverse=False) -> list[int]:
        # https://vk.com/@bookflow-naglyadnaya-vizualizacii-algoritmov-sortirovki
        length = len(_src)
        for i in range(0, length - 1):
            already_sorted = True
            for j in range(0, length - 1 - i):
                if _reverse:
                    if _src[j] < _src[j + 1]:
                        # a = 15
                        # b = 17

                        # c = b
                        # b = a
                        # a = c

                        # a, b = b, a
                        # print(a, b)

                        _src[j], _src[j + 1] = _src[j + 1], _src[j]
                        already_sorted = False
                else:
                    if _src[j] > _src[j + 1]:
                        _src[j], _src[j + 1] = _src[j + 1], _src[j]
                        already_sorted = False
            if already_sorted:
                break
        return _src

    def sort_insertion(_src: list[int], _reverse=False) -> list[int]:
        length = len(_src)
        for i in range(1, length):
            key_item = _src[i]
            j = i - 1
            if _reverse:
                while j >= 0 and _src[j] < key_item:
                    _src[j + 1] = _src[j]
                    # j -= 1  # decrement
                    j = j - 1  # decrement
            else:
                while j >= 0 and _src[j] > key_item:
                    _src[j + 1] = _src[j]
                    j = j - 1
            _src[j + 1] = key_item

        return _src

    def sort_quicksort(_src: list[int], is_reversed=False) -> list[int]:
        def start_quicksort(__src: list[int], _is_reversed=False) -> list[int]:
            length = len(__src)
            if length < 2:
                return __src
            low, same, high = [], [], []
            pivot = __src[random.randint(0, length - 1)]
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

    if __name__ == "__main__":  # этот блок исполняется, только если файл запустить напрямую
        #          0  1  2   3                         9
        # list1 = [4, 5, 1, 333, 2, 3, 100, 42, 6, 60, 7]
        list1 = []
        for _ in range(1, 1000 + 1):
            list1.append(random.randint(1, 1000 + 1))
        is_reverse = False

        print("Оригинальный массив: ", list1)
        t_start = time.perf_counter()

        print("Стандартная сортировка: ", sort_sorted(list1, is_reverse))  # 0.00143
        print("Пузырьковая сортировка: ", sort_bubble(list1, is_reverse))  # 0.05709
        # print("Сортировка вставками: ", sort_insertion(list1, is_reverse))    # 0.02701
        # print("Сортировка быстрая: ", sort_quicksort(list1, is_reverse))      # 0.00699
        # print("Сортировка слиянием: ", sort_merge(list1, is_reverse))           # 0.00698

        t_stop = time.perf_counter()
        print("Заняло времени: ", round(t_stop - t_start, 5), " секунд")


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

def ex8():
    from collections import deque
    from typing import Optional

    def example():
        print("example")

    def divmod_palindrome_number():
        def solution(x: int) -> bool:
            if x < 0:
                return False

            new = 0
            orig = x
            while x:
                x, d = divmod(x, 10)
                new = new * 10 + d
            return new == orig

        print(solution(123))
        print(solution(121))
        print(solution(-121))
        pass

    def hash_contains_duplicate():
        def solution(nums: list[int]) -> bool:
            return len(nums) != len(set(nums))

        print(solution([1, 2, 3, 1]))
        print(solution([1, 2, 3, 4]))
        pass

    def linked_list_remove_linked_list_elements():
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

        def solution(head: Optional[ListNode], val: int) -> Optional[ListNode]:
            dummy = ListNode(None, next=head)
            cur = head
            prev = dummy
            while cur:
                if cur.val == val:
                    prev.next = cur.next
                else:
                    prev = cur
                cur.next = cur.next

            return dummy.next

        print(solution([1, 2, 6, 3, 4, 5, 6], 6))
        print(solution([7, 7, 7, 7], 7))
        pass

    def bitwise_counting_bits():
        def solution(n: int) -> list[int]:
            ans = [0]
            for i in range(1, n):
                cur = 0
                while i:
                    cur += i & 1
                    i >>= 1
                ans.append(cur)
            return ans

        print(solution(2))
        print(solution(5))
        pass

    def hash_unique_email_addresses():
        def solution(emails: list[str]) -> int:
            unique = set()
            for e in emails:
                name, dom = e.split('@')
                name = name.split("+")[0]
                name = name.replace('.', '')
                unique.add(f"{name}@{dom}")
            return len(unique)

        print(solution(["bogdan.1@mail.com", "bogdan1@mail.com", "bogdan1@mail.ru"]))
        pass

    def sliding_window_maximum_awerage_subarray():
        def solution(nums: list[int], k: int) -> float:
            cur = sum(nums[:k])
            cur_max = cur
            for i in range(k, len(nums)):
                cur -= nums[i - k]
                cur += nums[i]
                cur_max = max(cur, cur_max)
            return cur_max / k

        print(solution([1, 12, -5, -6, 50, 3], 4))
        pass

    def two_pointers_move_zeroes():
        def solution(nums: list[int]) -> None:
            j = 0
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
            print(nums)

        print(solution([0, 1, 0, 3, 12]))
        pass

    def binary_search_valid_perfect_square():
        def solution(num: int) -> bool:
            if num == 1:
                return True
            l, r = 1, num // 2
            while l <= r:
                mid = (l + r) // 2
                sq = mid * mid
                if sq == num:
                    return True
                if sq < num:
                    l = mid + 1
                else:
                    r = mid - 1
            return False

        print(solution(16))
        print(solution(50))
        print(solution(1))
        pass

    def divmod_add_digits():
        def solution(num: int) -> int:
            while num >= 10:
                cur = num
                new_num = 0
                while cur:
                    cur, d = divmod(cur, 10)
                    new_num += d
                num = new_num
            return num

        print(solution(38))
        print(solution(0))
        pass

    def string_student_attendance_record():
        def solution(s: str) -> bool:
            l_cnt = 0
            a_cnt = 0
            for c in s:
                if c == "A":
                    a_cnt += 1
                    if a_cnt == 2:
                        return False
                if c == "L":
                    l_cnt += 1
                    if l_cnt > 2:
                        return False
                else:
                    l_cnt = 0
            return True

        print(solution("PPALLP"))
        print(solution("PPALLL"))
        pass

    def tree_binary_tree_postorder_traversal():
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

        def solution(root: Optional[TreeNode]) -> list[int]:
            ans = []

            def helper(node):
                if node:
                    helper(node.left)
                    helper(node.right)

                    ans.append(node.val)

            helper(root)
            return ans

        print([1, None, 2, 3])
        print([])
        pass

    def stack_is_subsequence():
        def solution(s: str, t: str) -> bool:
            stack = list(s)[::-1]

            for c in t:
                if stack and stack[-1] == c:
                    stack.pop()
            return len(stack) == 0

        print(solution('abc', "ahbgdc"))
        print(solution('axc', "ahbgdc"))
        pass

    def tree_symmetric_tree():
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

        def solution(root: Optional[TreeNode]) -> bool:
            q = deque([root])
            levels = []
            while q:
                level = []
                for _ in range(len(q)):
                    cur = q.popleft()
                    level.append(cur.val if cur else None)
                    if cur:
                        q.append(cur.left)
                        q.append(cur.right)

                if len(level) < 1:
                    n = len(level)
                    if level[:n // 2] != level[n // 2:][::-1]:
                        return False
            return True

        print(solution([1, 2, 2, 3, 4, 4, 3]))
        print(solution([]))
        pass

    def divmod_plus_one():
        def solution(digits: list[int]) -> list[int]:
            carry = 1
            for i in range(len(digits) - 1, -1, -1):
                carry, digits[i] = divmod(digits[i] + carry, 10)
            return digits if not carry else [carry] + digits

        print(solution([1, 2, 3]))
        print(solution([4, 3, 2, 1]))
        pass

    def sorting_meeting_rooms():
        def solution(intervals: list[list[int]]) -> bool:
            intervals.sort()
            for i in range(1, len(intervals)):
                if intervals[i][0] < intervals[i - 1][1]:
                    return False
            return True

        print(solution([[0, 30], [45, 50]]))
        print(solution([[0, 30], [5, 10], [15, 20]]))
        print(solution([[0, 30], [5, 10], [15, 20]]))
        pass

    def linked_list_middle_of_the_linked_list():
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

        def solution(head: Optional[ListNode]) -> Optional[ListNode]:
            slow = head
            fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        print(solution([1, 2, 3, 4, 5]))
        print(solution([3, 4, 5]))
        pass

    def hash_check_if_n_and_its_double_exists():
        def solution(arr: list[int]) -> bool:
            seen = set()
            for num in arr:
                if num * 2 in seen or num / 2 in seen:
                    return True
                seen.add(num)
            return False

        print(solution([10, 2, 5, 3]))
        print(solution([7, 1, 14, 11]))
        pass

    def dp_n_th_tribonacci_number():
        def solution(n: int) -> int:
            dp = [0, 1, 1]
            if n < 3:
                return dp[n]
            for i in range(3, n + 1):
                dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])
            return dp[-1]

        print(solution(4))
        print(solution(25))
        pass

    def binary_search_binary_search():
        def solution(nums: list[int], target: int) -> int:
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            return -1

        print(solution([-1, 0, 3, 5, 9, 12], 9))
        print(solution([-1, 0, 3, 5, 9, 12], 2))
        pass

    def dp_pascale_triangle():
        def solution(num_rows: int) -> list[list[int]]:
            dp = [[1], [1, 1]]
            if num_rows < 3:
                return dp[:num_rows]
            for _ in range(num_rows - 2):
                next_row = [1]
                for i in range(1, len(dp[-1])):
                    next_row.append(dp[-1][i] + dp[-1][i - 1])

                next_row += [1]
                dp.append(next_row)

            return dp

        print(solution(5))
        print(solution(1))
        pass

    def bitwise_single_number():
        def solution(nums: list[int]) -> int:
            ans = 0
            for num in nums:
                ans ^= num

            return ans

        print(solution([2, 2, 1]))
        print(solution([4, 1, 2, 1, 2]))
        pass

    def binary_search_peak_index_in_a_mountain_array():
        def solution(arr: list[int]) -> int:
            l, r = 0, len(arr) - 1
            while l < r:
                mid = (l + r) // 2
                if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                    return mid
                if arr[mid] > arr[mid - 1]:
                    l = mid
                else:
                    r = mid
            pass

        print(solution([0, 1, 0]))
        print(solution([0, 2, 1, 0]))
        pass

    def two_pointers_valid_palindrome():
        def solution(arr: list[int]) -> int:
            pass

        print(solution([0, 1, 0]))
        print(solution([0, 2, 1, 0]))
        pass

    if __name__ == "__main__":
        # асимптоматика
        # эвристика

        # divmod_palindrome_number()
        # hash_contains_duplicate()
        # linked_list_remove_linked_list_elements()
        # bitwise_counting_bits()
        # hash_unique_email_addresses()
        # sliding_window_maximum_awerage_subarray()
        # two_pointers_move_zeroes()
        # binary_search_valid_perfect_square()
        # divmod_add_digits()
        # string_student_attendance_record()
        # tree_binary_tree_postorder_traversal()
        # stack_is_subsequence()
        # tree_symmetric_tree()
        # divmod_plus_one()
        # sorting_meeting_rooms()
        # linked_list_middle_of_the_linked_list()
        # hash_check_if_n_and_its_double_exists()
        # dp_n_th_tribonacci_number()
        # binary_search_binary_search()
        # dp_pascale_triangle()
        # bitwise_single_number()
        # binary_search_peak_index_in_a_mountain_array()
        two_pointers_valid_palindrome()
        pass
