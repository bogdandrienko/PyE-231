########################################################################################################################
# TODO ООП
import datetime
import time


# Объектно-ориентированное программирование: способ представления взаимодействий сущностей как в реальной жизни

# Процедурное программирование Паскаль
# Объектно-ориентированное программирование  C#, Делфи, Python, С++
# Функциональное программирование F# Haskel

#                     объект - видимость, рендеринг, коллизии (физики)
#                     техника - скорость, масса, может с ними взаимодействовать
#         сухопутные водоплавающие - точки, где можно перемещаться
#  Велосипед Машина Мотоцикл гидро скутер Лодка - текстуры, цвет

# Наследование
# Инкапсуляция
# Полиморфизм
# Множественное наследование
# ...

# TODO простой пример
class Mother1:  # Mother1(object)
    eyes = "blue"


m1 = Mother1()  # инициализация класса (создание экземпляра)
print("цвет глаз матери: ", m1.eyes)


class Child(Mother1):  # Наследование от класса Mother1
    age = 7
    eyes = "green"  # override - переопределение - перезапись


c1 = Child()
print("цвет глаз ребёнка: ", c1.eyes)
print("возраст ребёнка: ", c1.age)


class Figure:
    pi = 3.1415
    e = 2.79
    name = "Квадрат"  # Переменная(атрибут) класса - доступна без создания экземпляра

    def __init__(self, side1: float | int, side2: float | int):  # методы - функции внутри класса
        self.name = "Прямоугольник"  # Переменная(атрибут) экземпляра класса - доступна только при создании экземпляра

        self.side1 = side1
        self.side2 = side2

        # time.sleep(5.1)
        # self.perimeter = (side1 + side2) * 2  # только если нагрузка небольшая (быстро и недорого по памяти)
        # self.area = side1 * side2

        self.description = "ПУБЛИЧНАЯ"  # public
        self._description = "ЗАЩИЩЁННАЯ"  # protected
        self.__description = "ПРИВАТНАЯ"  # private

    def get_perimeter(self):  # self - ссылка на себя
        time.sleep(0.1)
        return (self.side1 + self.side2) * 2

    def get_area(self):
        return self.side1 * self.side2 // 1.1

    def get_area_with_multiply(self, multiply: int | float) -> int | float:
        return self.get_area() * multiply

    # def area
    pass


print("\n\n\n\n")
f1 = Figure(10, 15)
print("Фигура1: ", f1.get_perimeter())
print("Фигура1: ", f1.get_area())
print("Фигура1: ", f1.name)
print("Фигура1: ", f1.description)
print("Фигура1: ", f1._description)  # TODO НЕ ЖЕЛАТЕЛЬНО
print("Фигура1: ", f1._Figure__description)  # TODO НЕЛЬЗЯ
print(Figure.name)

print("\n\n\n\n")

# print("Фигура1: ", f1.perimeter)
print("Фигура1: ", f1.get_perimeter())
print("Фигура1: ", f1.get_area())
print("Фигура1: ", f1.get_area_with_multiply(10))

print("\n\n\n\n")


class Calc:
    def __init__(self, val1: int | float, val2: int | float, action: str = "+"):
        self.val1 = val1
        self.val2 = val2
        self.action = action

    def get_result(self, action: str = None):
        if action is not None:
            self.action = action
        match self.action:
            case "+":
                return self.val1 + self.val2
            case "-":
                return self.val1 - self.val2
            case "*":
                return self.val1 * self.val2
            case _:
                raise Exception("Unknown action")


calc1 = Calc(12, 13, "+")
print(calc1.get_result())
print(calc1.get_result(action="-"))


class Transport:
    def __init__(self, name, mass, motor, price, speed):
        self.name = name
        self._mass = mass
        self.motor = motor
        self.price = price
        self.speed = speed  # публичная - видна во всех случаях

        self._multiplayer = 12  # защищённая - предупреждает, при попытке её извлечь вне собственного контекста
        self.__multiplayer = 10  # приватная - невидима везде, кроме собственного контекста

    def drive(self):
        return self._mass / self.motor

    def get_speed(self):
        return self.speed


Transport1 = Transport("Трактор", 2000, 400, 5000, 30)

print(Transport1)
print(type(Transport1))
print(Transport1.drive())
print(Transport1.speed)
print(Transport1._mass)
print(Transport1._multiplayer)


class Water(Transport):
    def __init__(self, speed, *args):
        super().__init__(*args)

        self.speed1 = speed

    def drive(self):
        return super().drive() / 0.85

    def get_old_speed(self):
        return super().get_speed()


Transport2 = Water(1000, "Катамаран", 500, 20, 700, 15)

print(Transport2)
print(type(Transport2))
print(Transport2.drive())
print(Transport2.speed)
print(Transport2.speed1)


class SubWater(Water):
    def __init__(self, *args, **kwargs):  # args - позиционные - кортеж, kwargs - именные - словарь
        super().__init__(*args, **kwargs)

    def drive(self):
        return super().drive() * 1.5


Transport3 = Water(333333, "Подлодка", 333, 33, 3333, 3)

dict1 = {"speed": 12}
val1 = dict1.get("speed", "")
val2 = dict1["speed"]

print(Transport3)
print(type(Transport3))
print(Transport3.drive())
print(Transport3.speed)
print(Transport3._mass)
print(Transport3.speed1)
print(Transport3.get_speed())


########################################################################################################################

########################################################################################################################
# TODO статические методы

class Utils:
    class DateTimeC:
        @staticmethod  # статический (не имеет отношения к экземпляру) метод
        def get_time():
            return datetime.datetime.now().strftime("%Y")

        @staticmethod
        def get_different_times_in_seconds(datetime1: datetime.datetime, datetime2: datetime.datetime) -> int:
            # datetime1 - datetime2
            return 0


print(Utils.DateTimeC.get_time())

########################################################################################################################

########################################################################################################################
# TODO множественное наследование

class Mother2:
    val1 = 12

    def __init__(self, val1, name="Мама") -> None:
        self.name = name
        self.val = val1
        self._val = val1  # защищённый
        self.__val2 = val1 + 5  # приватный

    def get_value(self):
        return 777

    def __str__(self):
        return self.name





class Father2:
    val2 = 13

    def __init__(self, val1) -> None:
        self.val1 = val1

    def get_value(self):
        return 888

    def __str__(self):
        return self.val1


class Child2(Father2, Mother2):

    def __init__(self, val1) -> None:
        super().__init__(val1)

    # def get_value(self):
    #     return 666


print(Mother2.val1)
a1 = Mother2(10)
print(a1.val)
# print(a1._Mother__val2)

ch1 = Child2(10)
print("\n\n\n")
print(ch1.get_value())


########################################################################################################################

########################################################################################################################
# TODO classmethod and staticmethod
from datetime import date

class Person:
    def __init__(self, name: str, age: int | float):
        self.name = name
        self.age = age

    @classmethod  # - помогает конструировать класс
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod  # - не требует экземпляра для вызова
    def is_adult(age: int | float) -> bool:
        return age > 18


person1 = Person('Maya', 21)
person2 = Person.from_birth_year('Maya', 1996)

print(person1.age)
print(person2.age)

print(Person.is_adult(22))