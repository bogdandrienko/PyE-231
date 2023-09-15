# Наследование
import datetime


class Mother1:  # (object)
    eyes = "blue"  # Атрибут класса

    def cook(self):
        pass


class Child1(Mother1):
    eyes = "black"
    height = 1.85

    def jump(self):  # метод (функция внутри класса называется методом)
        return f'My name is Joe. My eyes is {self.eyes}'  # из self. можно извлечь свои методы, и свои атрибуты/свойства



m1 = Mother1()  # инициализация(создание) экземпляра класса
c1 = Child1()
print(m1.eyes)
print(c1.eyes)
print(c1.height)
print(c1.jump())
print(c1.cook())


class Figure:
    PI = 3.14  # доступен и без создания экземпляра
    # атрибут класса - использовать редко, только для констант или каких-то наиболее неизменяемых значений

    def __init__(self, name, age=12):  # метод для инициализации __new__ - конструктор
        self.name = name  # атрибут экземпляра класса
        self.age = age * 2  # атрибут экземпляра класса

    def __abs__(self):
        # absolute - число по модулю
        pass
    def __len__(self) -> int:
        print("Я не имею длины")
        return 0

    def __add__(self, other):
        # 1. Сложить их площади
        # 2. Сложить их объёмы
        # 3. Сложить их массы
        pass
    def __eq__(self, other):  # dandre(магические) методы
        # equal
        pass

    def get_pi(self):
        return self.PI

    @staticmethod
    def static_get_pi():  # статический метод (не имеет ссылки на экземпляр)
        return Figure.PI


f1 = Figure(name="Квадрат")
print(len(f1))
print(f1.PI)
print(f1.get_pi())
print(Figure.static_get_pi())

class Utils:  # вспомогашка
    class DateTime:
        @staticmethod
        def get_current_year():
            return datetime.datetime.now().strftime("%Y")
        @staticmethod
        def get_current_time():
            return datetime.datetime.now()

print(Utils.DateTime.get_current_year())




print("\n\n\n\n\n\n.......\n\n\n\n\n\n")

print(Figure.PI)
# print(Figure.name)  # type object 'Figure' has no attribute 'name'
f2 = Figure(name="Квадрат Малевича")
print(f2.PI)
print(f2.name)




