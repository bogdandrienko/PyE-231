"""
views - контроллеры(вью) - т.е. бизнес логика
"""
from django.contrib.auth.models import User
from django.shortcuts import render
import sqlite3
from django_app import utils


@utils.decorator_error_handler
def home(request):
    # возврат HTML страницы
    return render(request, 'home.html', context={})


def blank(request):
    if request.method == 'GET':
        # тут база данных не нужна
        return render(request, 'blank.html', context={})
    elif request.method == 'POST':
        print("ПОЛУЧИЛИ РЕЗЮМЕ ОТ ЧЕЛОВЕКА")
        print("СОХРАНЯЕМ В БАЗУ ДАННЫХ")
        print('Request POST')

        print(request.GET)  # ?text=Python&area=6322 - query params
        print(request.POST)  # html form
        # print(request.body)  # bytes form
        # print(request.data)  # json data
        print(request.FILES)  # files

        fio = request.POST['fio']  # unsafe - если такого ключа нет, то возбуждается Exception
        # unsafe - используется, когда нужно вызывать ошибку при отсутствии ключа
        patronomyc = request.POST.get('patronomyc', '')  # safe - если такого ключа нет, то верётся default
        iin = 970810351176
        experience = "2 года"

        # create db
        utils.execute_sql(
            is_many=True,
            _source="users.db",
            _query="""
        CREATE TABLE IF NOT EXISTS profile (
            id INTEGER PRIMARY KEY UNIQUE NOT NULL,
            iin INTEGER NOT NULL UNIQUE,
            fio TEXT NOT NULL,
            experience REAL default 0.0);""",
            _kwargs={}
        )

        # ORM - object relative mapping - python-like SQL
        # user = User.objects.create(username="", email="", password="")
        # user.

        # create user
        utils.execute_sql(
            is_many=False,
            _source="users.db",
            _query=f"""
INSERT INTO profile (iin, fio, experience)
VALUES (:iin, :fio, :experience);
""",
            _kwargs={"iin": iin, "fio": fio, "experience": experience}
        )

        _users = utils.execute_sql(
            is_many=True,
            _source="users.db",
            _query="""
        SELECT id, iin, fio, experience FROM profile order by iin DESC;""",
            _kwargs={}
        )
        print("users: ", _users)

        # тут не нужен html
        # todo REDIRECT(перенаправление)
        return render(request, 'blank.html', context={"message": "Ваше резюме успешно отправлено!"})


def database():
    # todo Создание таблицы
    utils.execute_sql(is_many=True, _source="database.db", _kwargs={}, _query="""
    CREATE TABLE IF NOT EXISTS profile (
        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
        iin INTEGER NOT NULL UNIQUE,
        fio TEXT NOT NULL,
        experience REAL default 0.0);""")

    # todo Чтение всех пользователей с сортировкой по iin
    _users = utils.execute_sql(is_many=True, _source="database.db", _kwargs={}, _query="""
SELECT id, iin, fio, experience FROM profile order by iin DESC;""")

    # todo Чтение пользователя с сортировкой по iin

    #         _users = utils.execute_sql(is_many=False, _source="database.db",  _kwargs={}, _query="""
    # SELECT id, iin, fio, experience FROM profile WHERE iin = '970810351179';""")  # захардкоженные

    iin = 970810351179
    #         _users = utils.execute_sql(is_many=False, _source="database.db",  _kwargs={}, _query=f"""
    # SELECT id, iin, fio, experience FROM profile WHERE iin = '{iin}';""")  # TODO SQL INJECTION!!!

    _users = utils.execute_sql(is_many=False, _source="database.db", _query=f"""
SELECT id, iin, fio, experience FROM profile WHERE iin = :iin;""", _kwargs={"iin": iin})  # TODO SQL SAFE

    # todo Вставка пользователя
    _users = utils.execute_sql(is_many=False, _source="database.db", _query=f"""
INSERT INTO profile (iin, fio, experience)
VALUES (:iin, :fio, :experience);""", _kwargs={"iin": iin, "fio": iin, "experience": iin})  # TODO SQL SAFE
