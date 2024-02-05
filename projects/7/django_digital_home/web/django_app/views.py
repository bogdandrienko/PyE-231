import datetime
import json
import sqlite3
from django.http import JsonResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from django_app import utils

# TODO - DRF


def home(request):
    _rows = utils.Sql.sql_execute(
        _query="""
            SELECT key, value 
            FROM params;""",  # TODO WHERE serial_id
        _kwargs={},
        _source="local_settings.db",
    )
    _dict = [{"key": str(x[0]), "value": str(x[1])} for x in _rows]
    _params = {}
    for i in _dict:
        _params[i["key"]] = i["value"]
    # print("_params: ", _params)
    return render(request, "Home.html", context={"params": _params})


def api_native(request: HttpRequest) -> JsonResponse:
    """проверка пинга, т.е. уходят или приходят ли запросы"""
    return JsonResponse(data={"message": "OK"})


@api_view(http_method_names=["GET", "POST", "PUT", "PATCH", "DELETE"])
def api(request: Request) -> Response:
    """проверка пинга, т.е. уходят или приходят ли запросы"""
    return Response(data={"message": "OK"})


@api_view(http_method_names=["GET", "POST"])
@utils.DRF.decor_error
def params(request: Request) -> dict:
    """Возвращает(GET)/вставляет(POST) или обновляет(POST) параметры
    конкретного холодильника по 'serial_id'"""

    if request.method == "GET":
        # TODO проверить токен

        # получаем данные с клиента (query_params)
        _serial_id = str(request.query_params["serial_id"])  # http://127.0.0.1:8000/api/params/?serial_id=97080135

        # получаем данные с базы
        _rows = utils.Sql.sql_execute(
            _query=f"""
SELECT serial_id, params
FROM params_by_serial_id
WHERE serial_id = :serial_id
;""",
            _kwargs={"serial_id": _serial_id},
            _source="params.db",
        )

        # возвращаем на клиент
        _response = {"serial_id": _serial_id, "params": json.loads(_rows[0][1])}
        return {"data": _response}
    elif request.method == "POST":
        # TODO проверить токен

        # получаем данные с клиента (json)
        _data = request.data
        _serial_id = _data["serial_id"]
        _params = json.dumps(_data["params"])

        # обновляем базу данных
        """
        Обновить или вставить новую строку.
        1Проверить, есть ли строка, если есть - 2обновить, если нет - 3вставить.
        """
        utils.Sql.sql_execute(
            _query=f"""
INSERT OR REPLACE 
INTO params_by_serial_id
    (serial_id, params)
VALUES
    (:serial_id, :params)
;""",
            _kwargs={"serial_id": _serial_id, "params": _params},
            _source="params.db",
        )
        return {"message": "Successfully created/updated"}


@api_view(http_method_names=["GET", "POST"])
@utils.DRF.decor_error
def messages(request: Request) -> dict:
    """"""

    if request.method == "GET":
        # TODO проверить токен

        # получаем данные с клиента (query_params)
        _serial_id = str(request.query_params["serial_id"])  # http://127.0.0.1:8000/api/messages/?serial_id=97080135

        # получаем данные с базы
        _rows = utils.Sql.sql_execute(
            _query=f"""
SELECT serial_id, date_time_subsystem_timestamp, date_time_server_timestamp, params
FROM messages_by_serial_id
WHERE serial_id = :serial_id
;""",
            _kwargs={"serial_id": _serial_id},
            _source="messages.db",
        )
        _dict = [
            {
                "serial_id": str(x[0]),
                "date_time_subsystem": datetime.datetime.fromtimestamp(x[1]),
                "date_time_server": datetime.datetime.fromtimestamp(x[2]),
                "params": json.loads(x[3]),
            }
            for x in _rows
        ]
        _dict = sorted(_dict, key=lambda x: x["date_time_subsystem"], reverse=True)

        # возвращаем на клиент
        _response = {"messages": _dict}
        return {"data": _response}
    elif request.method == "POST":
        # TODO проверить токен

        # получаем данные с клиента (json)
        _data = request.data
        _serial_id = _data["serial_id"]
        _date_time_subsystem = datetime.datetime.strptime(_data["date_time_subsystem"], "%Y-%m-%d %H:%M:%S.%f")
        _params = json.dumps(_data["params"])
        _date_time_server = datetime.datetime.now()

        # вставляем сообщение в базу данных
        utils.Sql.sql_execute(
            _query=f"""
INSERT INTO messages_by_serial_id
    (serial_id, date_time_subsystem_timestamp, date_time_server_timestamp, params)
VALUES
    (:serial_id, :date_time_subsystem_timestamp, :date_time_server_timestamp, :params)
;""",
            _kwargs={"serial_id": _serial_id, "date_time_subsystem_timestamp": _date_time_subsystem.timestamp(), "date_time_server_timestamp": _date_time_server.timestamp(), "params": _params},
            _source="messages.db",
        )

        return {"message": "Successfully created/updated"}


# TODO OLD #############################################################################


def settings_change(request) -> dict:
    # print("request.GET: ", request.GET)
    name = request.GET["name"]
    action = request.GET["action"]

    _rows = utils.Sql.sql_execute(
        _query="""
        SELECT key, value 
        FROM params;""",  # TODO WHERE serial_id
        _kwargs={},
        _source="local_settings.db",
    )
    _dict = [{"key": str(x[0]), "value": str(x[1])} for x in _rows]
    _params = {}
    for i in _dict:
        _params[i["key"]] = i["value"]
    _value = int(_params.get(name, 0))
    if action == "plus":
        _value += 1
    elif action == "minus":
        _value -= 1
    else:
        print("unknown action!")

    utils.Sql.sql_execute(
        _query="""
    INSERT OR REPLACE 
    INTO params
        (key, value)
    VALUES
        (:key, :value)
    ;""",  # TODO WHERE serial_id = '_data["id"]'
        _kwargs={"key": str(name), "value": str(_value)},
        _source="local_settings.db",
    )

    return redirect(reverse("home"))
