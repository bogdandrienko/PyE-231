# 1. Алгоритмы встречаются чаще на высоких нагрузках
# кэш, позволяет ускорить получение данных от 100 до 100000
import random
import time

# 3 s = 1(10 000 * 0.01s) s + 1(10 000 * 0.01s) s + 1(10 000 * 0.01s) s
# 300

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


s=input()
stack=[]
is_good=True
for i in s:
if i in "({[":
stack.append(i)
elif i in ")}]":
if not stack:
is_good=False
break
open_bracket=stack.pop()
if open_bracket=="(" and i==")":
continue
if open_bracket=="[" and i=="]":
continue
if open_bracket=="{" and i=="}":
continue
is_good=False
break

if is_good and len(stack)==0:
print("balanced")
else:
print("not balanced")