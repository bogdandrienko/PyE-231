import json
import sqlite3
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django_app import utils


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
    return render(request, 'Home.html', context={"params": _params})


def index(request):
    return JsonResponse(data={"message": "OK"})


@utils.auth_paramaterized_decorator(_token="Token=auth123")
def settings_get(request) -> dict:
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
    _data = {
        "temp_plan_high": _params["temp_plan_high"],
        "temp_plan_down": _params["temp_plan_down"]
    }
    return {"data": _data}


@csrf_exempt
@utils.auth_paramaterized_decorator(_token="Token=auth1234")
def settings_set(request) -> dict:
    # print(request.POST)
    # print(request.body)

    _data = json.loads(request.body.decode("utf-8"))
    # TODO уникальный ключ для серийного номера холодильника serial_id
    for k, v in _data["params"].items():
        utils.Sql.sql_execute(
            _query="""
    INSERT OR REPLACE 
    INTO params
        (key, value)
    VALUES
        (:key, :value)
    ;""",  # TODO WHERE serial_id = '_data["id"]'
            _kwargs={"key": str(k), "value": str(v)},
            _source="local_settings.db",
        )
    # print(_data)
    # with open("database.txt", "w") as f:
    #     f.write(f"""""")

    return {"data": 'OK'}


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
