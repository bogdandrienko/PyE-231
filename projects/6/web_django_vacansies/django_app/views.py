"""
views - контроллеры(вью) - т.е. бизнес логика
"""
import json
import random
import time
from django.contrib.auth.hashers import make_password
from django.core.cache import caches
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
import sqlite3

from django.urls import reverse
from django.views.decorators.cache import cache_page
from django_app import utils, models
from django_vacansie.models import Vacansie

# наш собственный кэш
cache: utils.CustomCache = utils.CustomCache()
# get/set
RamCache = caches["default"]
DatabaseCache = caches["special"]
# RedisCache = caches["extra"]


# @utils.decorator_error_handler
def home(request):
    # возврат HTML страницы
    return render(request, "home.html", context={})


def blank(request):
    if request.method == "GET":
        # тут база данных не нужна
        return render(request, "blank.html", context={})
    elif request.method == "POST":
        print("ПОЛУЧИЛИ РЕЗЮМЕ ОТ ЧЕЛОВЕКА")
        print("СОХРАНЯЕМ В БАЗУ ДАННЫХ")
        print("Request POST")

        print(request.GET)  # ?text=Python&area=6322 - query params
        print(request.POST)  # html form
        # print(request.body)  # bytes form
        # print(request.data)  # json data
        print(request.FILES)  # files

        fio = request.POST["fio"]  # unsafe - если такого ключа нет, то возбуждается Exception
        # unsafe - используется, когда нужно вызывать ошибку при отсутствии ключа
        patronomyc = request.POST.get("patronomyc", "")  # safe - если такого ключа нет, то верётся default
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
            _kwargs={},
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
            _kwargs={"iin": iin, "fio": fio, "experience": experience},
        )

        _users = utils.execute_sql(
            is_many=True,
            _source="users.db",
            _query="""
        SELECT id, iin, fio, experience FROM profile order by iin DESC;""",
            _kwargs={},
        )
        print("users: ", _users)

        # тут не нужен html
        # todo REDIRECT(перенаправление)
        return render(request, "blank.html", context={"message": "Ваше резюме успешно отправлено!"})


@utils.decorator_time_measure
def test(request):
    # key = "_users"
    # _users = cache.get(key=key)
    # if _users is None:
    #     _users = utils.execute_sql(
    #         is_many=True,
    #         _source="users.db",
    #         _query="""SELECT id, iin, fio, experience FROM profile order by iin DESC;""",
    #         _kwargs={},
    #     )
    #     time.sleep(0.005)
    #     cache.set(key=key, value=_users, lifetime_s=5)
    # return HttpResponse(json.dumps(_users, ensure_ascii=False))

    key = "_users"
    _users = RamCache.get(key)
    if _users is None:
        # ORM - object relative mapping - python-like(похожий на Python)
        # SQL - есть минусы
        """SELECT id, iin, fio, experience FROM profile order by iin DESC;"""
        _json = User.objects.all().order_by("-id")
        _users = []
        for user in _json:
            _users.append({"id": user.id, "username": user.username, "email": user.email, "password": user.password})
        RamCache.set(key, _users, timeout=5)
    time.sleep(1.0)

    """
Без кэша -  0.0135
С кэшом -   0.0023
х6 = +600%

Чем тяжелее груз(запрос к базе данных) тем эффективнее остаться дома(взять из кэша).
    """

    # for i in range(1, 1000):
    #     usr = f"Bogdan {i}"
    #     User.objects.create(username=usr, email=usr + "@mail.ru", password=make_password(usr))
    return HttpResponse(json.dumps(_users, ensure_ascii=False))


def database():
    # todo Создание таблицы
    utils.execute_sql(
        is_many=True,
        _source="database.db",
        _kwargs={},
        _query="""
    CREATE TABLE IF NOT EXISTS profile (
        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
        iin INTEGER NOT NULL UNIQUE,
        fio TEXT NOT NULL,
        experience REAL default 0.0);""",
    )

    # todo Чтение всех пользователей с сортировкой по iin
    _users = utils.execute_sql(
        is_many=True,
        _source="database.db",
        _kwargs={},
        _query="""
SELECT id, iin, fio, experience FROM profile order by iin DESC;""",
    )

    # todo Чтение пользователя с сортировкой по iin

    #         _users = utils.execute_sql(is_many=False, _source="database.db",  _kwargs={}, _query="""
    # SELECT id, iin, fio, experience FROM profile WHERE iin = '970810351179';""")  # захардкоженные

    iin = 970810351179
    #         _users = utils.execute_sql(is_many=False, _source="database.db",  _kwargs={}, _query=f"""
    # SELECT id, iin, fio, experience FROM profile WHERE iin = '{iin}';""")  # TODO SQL INJECTION!!!

    _users = utils.execute_sql(
        is_many=False,
        _source="database.db",
        _query=f"""
SELECT id, iin, fio, experience FROM profile WHERE iin = :iin;""",
        _kwargs={"iin": iin},
    )  # TODO SQL SAFE

    # todo Вставка пользователя
    _users = utils.execute_sql(
        is_many=False,
        _source="database.db",
        _query=f"""
INSERT INTO profile (iin, fio, experience)
VALUES (:iin, :fio, :experience);""",
        _kwargs={"iin": iin, "fio": iin, "experience": iin},
    )  # TODO SQL SAFE


# TODO NEW #############################################################################################


@utils.decorator_time_measure
def vacansie_list(request):
    # fake
    # vacs = [{"title": f"Вакансия №{x}"} for x in range(1, 100 + 1)]

    # генерация набора данных в базе
    # words = ["пекарь", "водитель", "программист"]
    # for i in range(1, 30):
    #     models.Vacansie.objects.create(title=f"{random.choice(words)} {i}", description="Описание вакансии", salary=100000 + i * 30, is_active=True)

    # orm
    # vacs = models.Vacansie.objects.all().filter(is_active=True)
    vacs = utils.get_cache("vacansie_list", lambda: Vacansie.objects.all().filter(is_active=True), timeout=20)

    # 0.0015
    # 0.0005 -> 3x - 300%

    return render(request, "vacansie/vacansie_list.html", context={"vacs": vacs})
