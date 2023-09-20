import sqlite3
import datetime

from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")


# http://127.0.0.1:8000/

# MVC(MVT)
# M - model(database) - raw data
# V - view - business-logic
# T - template(html) - display data

# model - # database (максимально сырые данные)


class User:
    def __init__(self, first_name, last_name, iin, category, is_active, date_time):
        if len(first_name) < 3:
            raise Exception("User must have at least 3 characters")
        self.first_name = first_name
        self.last_name = last_name
        self.iin = iin
        self.category = category
        self.is_active = is_active
        self.date_time = date_time

    def get_all_params(self) -> tuple:
        return self.first_name, self.last_name, self.iin, self.category, self.is_active, self.date_time


class DataBase:
    @staticmethod
    def create_database_file():
        query = """
CREATE TABLE IF NOT EXISTS User
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT NOT NULL,
last_name TEXT,
iin INTEGER UNIQUE NOT NULL,
category TEXT NOT NULL,
is_active INTEGER,
date_time TEXT default NOW()
)
"""
        with sqlite3.connect("database.db") as connection:
            cursor = connection.cursor()
            cursor.execute(query, ())
            connection.commit()

    @staticmethod
    def create_user(user: User):
        query = """
INSERT INTO User (first_name, last_name, iin, category, is_active, date_time)
VALUES           (?,             ?,       ?,     ?,        ?,         ?)
"""
        with sqlite3.connect("database.db") as connection:
            cursor = connection.cursor()
            cursor.execute(query, user.get_all_params())
            connection.commit()

    @staticmethod
    def get_all_users():
        query = """
SELECT * from User
"""
        with sqlite3.connect("database.db") as connection:
            cursor = connection.cursor()
            cursor.execute(query, ())
            rows = cursor.fetchall()
            return rows


@app.route("/")  # URL - маршрут(route/ссылка)
def index():  # VIEW - (бизнес-логика)
    # MODEL - просто тут не нужен
    return render_template('Index.html')  # TEMPLATE - отображение


@app.route("/pricing")
def pricing():
    return render_template('Pricing.html')


@app.route("/about")
def about():
    return "Привет, я просто строка"


@app.route("/api")
def api():
    return {"message": "OK"}


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('Register.html')
    elif request.method == 'POST':
        form = request.form
        first_name = form['firstName']  # unsafe - Exception
        last_name = form.get('lastName', "")  # safe - default = ''
        iin = form['iin']
        category = form.get('category', '')
        is_active = True
        date_time = datetime.datetime.now()
        if len(category) < 1:
            raise Exception("Категория не задана!")
        user = User(
            first_name=first_name,
            last_name=last_name,
            iin=iin,
            category=category,
            is_active=is_active,
            date_time=date_time,
        )
        DataBase.create_user(user=user)

        return render_template('Register.html', result="Успешно создано")


# TODO НАСЛЕДОВАНИЕ ###########################################
class Worker:
    name = ""

    def get_salary(self):
        print("Дайте зарплату!")


class Buh(Worker):
    pass


class Designer(Worker):
    pass


# b1 = Buh()
# d1 = Designer()
#
# d1.get_salary()


# TODO НАСЛЕДОВАНИЕ ###########################################

# TODO Инкапсуляция(сокрытие) ##################################

if __name__ == "__main__":
    # DataBase.create_database_file()
    users = DataBase.get_all_users()
    for i in users:
        print(i)

    class Timer:
        # атрибуты(свойства) класса
        VAL = 0

        def __init__(self):
            #  атрибуты(свойства) экземпляра класса (доступны только при создании)
            self.index = 666  # public(публичный - открытый) - служит для получения и изменения
            self._multiplayer = 777  # protected(защищённый - полу-закрытый) - служит для получения переменной в крайний случаях, либо только внутри класса
            self.__seconds = 888  # private(приватная - условно-закрытый) - служит для внутренних целей

        def change(self):  # метод(функция внутри класса)
            self._multiplayer *= 2  # допустимый уровень работы с protected

        def set_seconds(self, value):  # допустимый уровень работы с private
            self.__seconds = value

        def __eq__(self, other):  # магический метод(переопределение существующей логики)
            # eq = equal - равно (нужен, когда пытается сравнить этот класс с чем-то)
            pass

        def __len__(self):
            return int(self.__seconds ** 2)

        def __abs__(self):  # число по модулю
            pass

        @staticmethod
        def get_sum(a1, b1):  # статический метод(не нужен класс для вызова)
            return sum([a1, b1])


    # t1 = Timer()
    # print(t1.index)
    # print(t1._multiplayer)
    # # print(t1.__seconds)  # AttributeError: 'Timer' object has no attribute '__seconds'
    # print(t1._Timer__seconds)  # принудительный способ, получить переменную
    # t1.set_seconds(555)
    # print(t1._Timer__seconds)  # принудительный способ, получить переменную
    # print("lenght: ", len(t1))
    # print(Timer.get_sum(12, 13))

# TODO Инкапсуляция(сокрытие) ##################################
