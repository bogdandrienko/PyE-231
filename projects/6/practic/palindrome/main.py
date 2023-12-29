# 1. Языковая (Async, Threading, GIL, OOP...)
# 2. Алгоритмическая (leetcode)
# 3. Фреймворк
# 4. System Design (архитектура)

"""
Задача:
Поиск палиндрома

Описание задачи:
Напишите программу на языке Python, которая осуществляет поиск палиндрома в заданной строке.
Палиндромом считается строка, которая читается одинаково как слева направо, так и справа налево,
игнорируя пробелы, знаки препинания и регистр символов.

Требования:
Программа должна запрашивать у пользователя ввод строки.
После ввода строки программа должна вывести результат: является ли введенная строка палиндромом или нет.
В процессе проверки палиндрома программа должна игнорировать пробелы, знаки препинания и регистр символов.
Программа должна быть реализована с использованием функций для повторного использования кода.
В конце собрать в консольное приложение. (за константную память - метод двух указателей, <=o^2)

Введите строку: A man, a plan, a canal, Panama!
Результат: Эта строка - палиндром.

Введите строку: СОС, оно, мадам
Результат: Эта строка - палиндром.

Введите строку: Python is fun
Результат: Эта строка не является палиндромом.
"""


def is_palindrome_v1(_text: str) -> bool:
    """Синтаксический сахар - специализирован на Python"""

    # очистка от сторонних проблем
    if not isinstance(_text, str):
        return False
    if len(_text) <= 0:
        return False

    # очистка от всего, кроме букв
    clear = ""
    for i in _text:
        if i.isalpha():
            clear += i
    print("clear: ", clear)
    # clear = "".join([x for x in _text if x.isalpha()])

    # O(n) = 100c (линейная)
    # 2 * O(n) = 200c
    # O(n)^2 = 10000c (квадратичная)

    # сравнение
    return clear == clear[::-1]


def is_palindrome_v2(_text: str) -> bool:
    if not isinstance(_text, str):
        return False
    if len(_text) <= 0:
        return False

    l, r = 0, len(_text) - 1

    # 1. Чистка
    # clear = ""
    # for i in _text:
    #     if i.isalpha():  # буквы
    #         clear += i.lower()  # маленькие
    # print("clear: ", clear)

    # O(1)      = 1c (константная)
    # O(n)      = 100c (линейная)
    # O(2n)     = 200c
    # O(n^2)    = 10000c (квадратичная)

    # 2. Проверка
    while l <= r:  # O(N) - линейная
        # очистка l
        if not _text[l].isalpha():
            l = l + 1  # идёт вправо
            continue
        # очистка r
        if not _text[r].isalpha():
            r = r - 1  # идёт влево
            continue

        if _text[l].lower() != _text[r].lower():
            return False

        # смещение
        l = l + 1
        r = r - 1

    return True


while True:
    text: str = input("Введите строку для проверки: ")
    # text: str = "мадам"
    # text: str = "A man, a plan, a canal, Panama!"
    print(f"\nЭто палиндром!({text})" if is_palindrome_v2(text) else f"\nЭто не палиндром!({text})")

"""
pip install -U pyinstaller
pyinstaller --onefile main.py
"""
