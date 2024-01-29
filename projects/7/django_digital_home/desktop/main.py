import datetime
import json
import sys
import threading
import time
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication
import sqlite3
import requests


class Utils:
    HOST = '127.0.0.1'
    PORT = 8000

    class Query:
        @staticmethod
        def create_table_params() -> str:
            return f"""
CREATE TABLE IF NOT EXISTS params (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE NOT NULL,
    value TEXT NOT NULL DEFAULT ''
);"""

        @staticmethod
        def get_all_params() -> str:
            return f"""
SELECT key, value 
FROM params
;"""

        @staticmethod
        def get_insert_or_replace_params() -> str:
            return f"""
INSERT OR REPLACE 
INTO params
    (key, value)
VALUES
    (:key, :value)
;"""

    @staticmethod
    def sql_execute(_query: str, _kwargs: dict, _source: str):
        # TODO - WITH
        try:
            _connection = sqlite3.connect(f"src/database/{_source}")
            _cursor = _connection.cursor()
            _cursor.execute(_query, _kwargs)
            _connection.commit()
            _data = _cursor.fetchall()
            _cursor.close()
            _connection.close()
            return _data
        except Exception as error:
            print(error)

    @staticmethod
    def database_init():
        Utils.sql_execute(
            _query=Utils.Query.create_table_params(),
            _kwargs={},
            _source="local_settings.db",
        )

    @staticmethod
    def sync_settings_to_web():
        """
        TODO Sheduler(планировщик):
    - Нет смысла, в данном контексте, посылать исторические
    данные ночью в промежутке с 2 до 6.
        """
        # now = datetime.datetime.now()
        # time.sleep(59)
        # minute_list = [20]
        # hours_list = [x for x in range(0, 24)]
        # hours_list = [8, 20]
        # if now.hour not in hours_list and now.minute not in minute_list:
        #     print("skip")
        #     return

        # if datetime.datetime.now().hour != 20:
        #     return

        _rows = Utils.sql_execute(
            _query=Utils.Query.get_all_params(),
            _kwargs={},
            _source="local_settings.db",
        )
        _dict = [{"key": str(x[0]), "value": str(x[1])} for x in _rows]
        _params = {}
        for i in _dict:
            _params[i["key"]] = i["value"]

        try:
            _response = requests.post(
                url=f"http://{Utils.HOST}:{Utils.PORT}/api/settings/set/",
                headers={"Authorization": "Token=auth1234"},
                data=json.dumps({"id": "970801", "params": _params})
            )
            if _response.status_code not in (200, 201):
                # TODO логирование
                raise Exception(f"WEB ERROR {_response.status_code}")
        except Exception as error:
            print(error)

    @staticmethod
    def sync_settings_from_web():
        print("sync_settings_from_web")

        # TODO сохранять домен и порт в .json файле
        _response = requests.get(f"http://{Utils.HOST}:{Utils.PORT}/api/settings/get/", headers={"Authorization": "Token=auth123"})
        if _response.status_code not in (200, 201):
            raise Exception(f"WEB ERROR {_response.status_code}")
        _data = _response.json().get("data", {})
        # TODO нужен один запрос, а не цикл
        for k, v in _data.items():
            Utils.sql_execute(
                _query=Utils.Query.get_insert_or_replace_params(),
                _kwargs={"key": str(k), "value": str(v)},
                _source="local_settings.db",
            )

    @staticmethod
    def loop_constructor(_target: callable, _args: tuple, _delay: float | int, _prefix: str):
        while True:
            try:
                threading.Thread(target=_target, args=_args).start()
            except Exception as error:
                print(f"{datetime.datetime.now()} {_prefix}:", error)
            time.sleep(_delay)


class Ui(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("src/main.ui", self)
        self.__params = {}

        self.ui.pushButton_temp_plan_plus.clicked.connect(self.push_button_temp_plan_plus)
        self.ui.pushButton_temp_plan_minus.clicked.connect(self.push_button_temp_plan_minus)

        self.show()
        threading.Thread(target=self.loop, args=()).start()

    def push_button_temp_plan_plus(self):
        _rows = Utils.sql_execute(
            _query="""
SELECT key, value 
FROM params;""",
            _kwargs={},
            _source="local_settings.db",
        )
        _dict = [{"key": str(x[0]), "value": str(x[1])} for x in _rows]
        _params = {}
        for i in _dict:
            _params[i["key"]] = i["value"]

        _temp_plan_high = int(_params.get("temp_plan_high", -7)) + 1
        _temp_plan_down = int(_params.get("temp_plan_down", -20)) + 1
        _data = {"temp_plan_high": _temp_plan_high, "temp_plan_down": _temp_plan_down}

        for k, v in _data.items():
            Utils.sql_execute(
                _query="""
INSERT OR REPLACE 
INTO params
    (key, value)
VALUES
    (:key, :value)
;""",
                _kwargs={"key": str(k), "value": str(v)},
                _source="local_settings.db",
            )

        # TODo нужно, чтобы и без рабочего backend-а всё работало
        # TODO Человек может подряд нажать 8 раз вниз, нужно отправить на web только 1 раз
        # TODO есть задержка при ошибке отправки

        threading.Thread(target=Utils.sync_settings_to_web, args=()).start()

    def push_button_temp_plan_minus(self):
        _rows = Utils.sql_execute(
            _query="""
SELECT key, value 
FROM params;""",
            _kwargs={},
            _source="local_settings.db",
        )
        _dict = [{"key": str(x[0]), "value": str(x[1])} for x in _rows]
        _params = {}
        for i in _dict:
            _params[i["key"]] = i["value"]

        _temp_plan_high = int(_params.get("temp_plan_high", -7)) - 1
        _temp_plan_down = int(_params.get("temp_plan_down", -20)) - 1
        _data = {"temp_plan_high": _temp_plan_high, "temp_plan_down": _temp_plan_down}

        for k, v in _data.items():
            Utils.sql_execute(
                _query="""
        INSERT OR REPLACE 
        INTO params
            (key, value)
        VALUES
            (:key, :value)
        ;""",
                _kwargs={"key": str(k), "value": str(v)},
                _source="local_settings.db",
            )

        threading.Thread(target=Utils.sync_settings_to_web, args=()).start()

    def update_ui_from_local_settings(self):
        _rows = Utils.sql_execute(
            _query=Utils.Query.get_all_params(),
            _kwargs={},
            _source="local_settings.db",
        )
        _dict = [{"key": str(x[0]), "value": str(x[1])} for x in _rows]
        _params = {}
        for i in _dict:
            _params[i["key"]] = i["value"]

        self.__params["temp_plan_high"] = int(_params.get("temp_plan_high", -7))
        self.__params["temp_plan_down"] = int(_params.get("temp_plan_down", -20))

        self.ui.label_temp_plan_high.setText(str(self.__params["temp_plan_high"]))
        self.ui.label_temp_plan_down.setText(str(self.__params["temp_plan_down"]))

    def loop(self):
        def loop1():
            while True:
                try:
                    threading.Thread(target=self.update_ui_from_local_settings, args=()).start()
                except Exception as error:
                    print(f"{datetime.datetime.now()} update_ui_from_local_settings:", error)
                time.sleep(0.1)

        def loop2():
            while True:
                try:
                    threading.Thread(target=Utils.sync_settings_from_web, args=()).start()
                except Exception as error:
                    print(f"{datetime.datetime.now()} Utils.sync_settings_from_web:", error)
                time.sleep(3.0)

        # TODO разобраться, как оптимизировать цикличные задачи в потоках
        threading.Thread(target=loop1).start()
        threading.Thread(target=loop2).start()
        # threading.Thread(target=Utils.loop_constructor(_target=self.update_ui_from_local_settings, _args=(), _delay=0.1, _prefix="loop_update_ui"), args=()).start()
        # threading.Thread(target=Utils.loop_constructor(_target=Utils.sync_settings_from_web, _args=(), _delay=3, _prefix="loop_update_settings_from_web"), args=()).start()


if __name__ == "__main__":
    # TODO - заменить весь код на асинхронный
    # TODO - ЕДИНОЕ логирование в локальную бд, и цикл, который будет отправлять эти ошибки на сервер
    # TODO - скрипт для сборки "в одно нажатие" (очистить старую папку, собрать и скопировать вспомогательные файлы)
    # TODO - каждый цикл, должен перед выполнением проверить, жив ли главный цикл.

    Utils.database_init()
    app = QApplication(sys.argv)
    ui = Ui()
    sys.exit(app.exec())
