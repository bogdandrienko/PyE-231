import sqlite3

from django.http import JsonResponse


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
    def table_init():
        Sql.sql_execute(
            _query="""
            CREATE TABLE IF NOT EXISTS params (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE NOT NULL,
                value TEXT NOT NULL DEFAULT ''
            );""",
            _kwargs={},
            _source="local_settings.db",
        )

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
