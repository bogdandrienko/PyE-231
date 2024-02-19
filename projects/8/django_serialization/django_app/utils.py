import sqlite3
from functools import wraps
from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response


class Startup:
    @staticmethod
    def tables_init():
        Sql.sql_execute(
            _query=f"""
CREATE TABLE IF NOT EXISTS params_by_serial_id (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    serial_id TEXT UNIQUE NOT NULL,
    params TEXT NOT NULL
);""",
            _kwargs={},
            _source="params.db",
        )
        Sql.sql_execute(
            _query=f"""
CREATE TABLE IF NOT EXISTS messages_by_serial_id (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    serial_id TEXT NOT NULL,
    date_time_subsystem_timestamp INTEGER NOT NULL,
    date_time_server_timestamp INTEGER NOT NULL,
    params TEXT NOT NULL
);""",
            _kwargs={},
            _source="messages.db",
        )


class DRF:
    @staticmethod
    def decor_error(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            _request: Request = args[0]
            try:
                _response: dict = func(*args, **kwargs)
                return Response(data=_response, status=200)
            except Exception as error:
                print(error)
                # TODO ЛОГИРОВАНИЕ
                return Response(data={"error": str(error)}, status=500)

        return wrapper


def auth_paramaterized_decorator(_token: str = ""):
    def decor(func):
        def wrapper(*args, **kwargs):
            if args[0].headers.get("Authorization", "") != _token:
                return JsonResponse(data={"error": "Not valid token"}, status=401)
            try:
                _response: dict = func(*args, **kwargs)
                return JsonResponse(data=_response, status=200)
            except Exception as error:
                # TODO ЛОГИРОВАНИЕ
                return JsonResponse(data={"error": str(error)}, status=500)

        return wrapper

    return decor


class Sql:
    @staticmethod
    def sql_execute(_query: str, _kwargs: dict, _source: str):
        try:
            _connection = sqlite3.connect(f"database/{_source}")
            _cursor = _connection.cursor()
            _cursor.execute(_query, _kwargs)
            _connection.commit()
            _data = _cursor.fetchall()
            _cursor.close()
            _connection.close()
            return _data
        except Exception as error:
            print(error)
