import datetime
import sqlite3
import time

from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render
from django.core.cache import caches

RamCache = caches["default"]
DatabaseCache = caches["special"]


def decorator_error_handler(_func: callable):
    def wrapper(*args, **kwargs):
        _request: HttpRequest = args[0]
        try:
            _response = _func(*args, **kwargs)  # view
        except Exception as error:
            print(f"{datetime.datetime.now()} ERROR {_request.path}")
            # TODO: error log - логи ошибок
            # создавать файл, с записью в каждый час
            return render(_request, "error.html", context={})
        else:
            return _response
        finally:
            # TODO: action log - логи действий(переходы, клики...)
            pass

    return wrapper


def decorator_time_measure(_func: callable):
    def wrapper(*args, **kwargs):
        t_start = time.perf_counter()
        _response = _func(*args, **kwargs)
        print("Функция отработала за: ", round(time.perf_counter() - t_start, 10))
        return _response

    return wrapper


def execute_sql(_query: str, _kwargs: dict, is_many: bool = True, _source: str = "database.db"):
    """Boilerplate - прослойка кода"""

    with sqlite3.connect(f"database/{_source}") as connection:  # создание соединения (manage.py - точка входа)
        cursor = connection.cursor()  # создание курсора
        cursor.execute(_query, _kwargs)  # выполнение запроса
        connection.commit()  # сохрание в базе данных
        if is_many:
            return cursor.fetchall()  # выборка данных tuple(tuple(raw))
        return cursor.fetchone()  # выборка данных tuple(raw)


class CustomCache:
    """
    Sanic + aiosqlite


                Кэш - временное(time limit) сохранение в памяти(RAM+ / db+ / file).
                Лучше всего использовать топовые готовые решения.
                Redis - можно вынести на другой сервер, +производительный, +умеет сохранять локально.

                В момент сохранения кэша нужно запоминать время.
                Cron - каждые 5 минут, по всему массиву кэша с проверкой его времени.

                Ассоциативный массив - словарь, с уникальными ключами(хэширование).

                Обоснование(зачем):
                1. Есть api, для 10 000 запросов за 2 секунды.
                Выборка с базы данных стоит нам 0.0005s(условно)

                1 секунда работы - 5 000 * 0.006 = 30s процессорного времени.
                5 секунд работы = 150s процессорного времени.

                2. Есть api, 5 секундный кэш - 0.0017 = 35х = 3500% performance

            # Users = 1000 человек

        Время кэша 1с
        Без кэша -  0.0135
        С кэшом -   0.0023

        1. 0.0135 (холодный старт)
        2. 0.0023 * 99
        0.24с

        1. 0.0135 * 100
        1,35с

    """

    default_lifetime = 5  # seconds

    def __init__(self):
        self.store = {}  # наше хранилище(ассоциативный массив)

        # new_loop_killer = threading.Thread(self.loop_killer)
        # new_loop_killer.start()

    def set(self, key: str, value: any, lifetime_s: int) -> None:
        """Запись(write/set) - установка значения по ключу."""
        # SOLID - единичная ответственность
        self.store[key] = {"value": value, "datetime": datetime.datetime.now() + datetime.timedelta(seconds=lifetime_s)}

        # new_cache_killer = threading.Thread(self.killer, (key, lifetime_s))
        # new_cache_killer.start()

    def killer(self, key: str, lifetime_s: int):
        """Убивает кэш после определённой задержки"""

        time.sleep(lifetime_s)
        del self.store[key]

    def loop_killer(self):
        """Поедание ресурсов высокое. Race condition."""

        while True:
            time.sleep(1)
            for key, value in self.store.items():
                dt = value["datetime"]
                if dt < 10:
                    del self.store[key]

    def get(self, key: str, is_silent: bool = True) -> any:
        """Чтение(read/get) - получение значения по ключу."""

        if is_silent:
            # return {"value": value, "datetime": datetime.datetime.now()}
            val = self.store.get(key, None)
            # print("val: ", val)
            if val is None:
                print("КЭШа нет")
                return None
            dt: datetime.datetime = val.get("datetime", None)
            if dt:
                # TODO оптимизация
                # if datetime.datetime.now() > dt:
                if (datetime.datetime.now() - dt).total_seconds() > 0:
                    print("КЭШ устарел")
                    # TODO """Нет очистки кэша""", наверное можно удалять прям тут.
                    return None
                else:
                    print("КЭШ свежий")
                    return val.get("value", None)
            else:
                return None
        return self.store[key]["value"]


def get_cache(key: str, query: callable = lambda: any, timeout: int = 10, cache: any = RamCache) -> any:
    # @cache_page(5)  # чтобы кэш был валидным(правильный), нужно все параметры учитывать при задании ключа
    # request.GET.get("page", 1)
    # request.GET.get("page", 5)
    #  {request.GET.get('page', 1)}
    # limit = 10 | 100(всего! 1 страница)
    # key = "vacansie_list "
    # for k, v in request.GET.items():  # вытащил все query params
    #     key += f"{k}_{v}_"

    data = cache.get(key)
    if data is None:
        data = query()
        cache.set(key, data, timeout)
    return data


def native_paginate(request, object_list, per_page):
    selected_page = request.GET.get(key="page", default=1)
    page_objs = Paginator(object_list=object_list, per_page=per_page)
    page_obj = page_objs.page(number=selected_page)
    return page_obj
