import datetime
import sqlite3

from django.http import HttpRequest
from django.shortcuts import render


def decorator_error_handler(_func: callable):
    def wrapper(*args, **kwargs):
        _request: HttpRequest = args[0]
        try:
            _response = _func(*args, **kwargs)  # view
        except Exception as error:
            print(f"{datetime.datetime.now()} ERROR {_request.path}")
            # TODO: error log - логи ошибок
            # создавать файл, с записью в каждый час
            return render(_request, 'error.html', context={})
        else:
            return _response
        finally:
            # TODO: action log - логи действий(переходы, клики...)
            pass
    return wrapper

def execute_sql(_query: str, _kwargs: dict, is_many: bool = True, _source: str = 'database.db'):
    with sqlite3.connect(f"database/{_source}") as connection:  # создание соединения (manage.py - точка входа)
        cursor = connection.cursor()  # создание курсора
        cursor.execute(_query, _kwargs)  # выполнение запроса
        connection.commit()  # сохрание в базе данных
        if is_many:
            return cursor.fetchall()  # выборка данных tuple(tuple(raw))
        return cursor.fetchone()  # выборка данных tuple(raw)
