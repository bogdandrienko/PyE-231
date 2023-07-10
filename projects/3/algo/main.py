# 1. Алгоритмы встречаются чаще на высоких нагрузках
# кэш, позволяет ускорить получение данных от 100 до 100000

# 3 s = 1(10 000 * 0.01s) s + 1(10 000 * 0.01s) s + 1(10 000 * 0.01s) s
# 300

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


