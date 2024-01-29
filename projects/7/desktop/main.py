import datetime
import sys
import threading
import time

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication
import sqlite3
import requests


class Utils:
    @staticmethod
    def sql_execute(_query: str, _kwargs: dict, _source: str):
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


class Ui(QWidget):
    """
    На экране есть цифра(план температуры в холодильной камере)
    +1. Значение берётся из локальной базы данных.
    -2. Нужно брать изменения с определённой периодичностью из локальной базы данных.
    -3. Нужно брать изменения с определённой периодичностью из веб-сервера.
    -4. Есть кнопки, которые должны применять изменения в локальной базе.
    """

    """
    Преждевременная оптимизация - обычно плохо, значит рано начали оптимизацию.
    Sheduler(планировщик):
    - Нет смысла, в данном контексте, посылать исторические 
    данные ночью в промежутке с 2 до 6.
    """

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("src/main.ui", self)
        self.__params = {}

        self.ui.pushButton_temp_plan_plus.clicked.connect(self.push_button_temp_plan_plus)
        self.ui.pushButton_temp_plan_minus.clicked.connect(self.push_button_temp_plan_minus)

        self.show()
        threading.Thread(target=self.loop, args=()).start()

    def push_button_temp_plan_plus(self):
        """
        * TODO берём старые
        * TODO конвертируем и изменяем
        * TODO записываем в базу
        """
        print(f"{datetime.datetime.now()} start pushButton_temp_plan_plus")

        # TODO берём старые
        Utils.sql_execute(
            _query="""
        CREATE TABLE IF NOT EXISTS params (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE NOT NULL,
            value TEXT NOT NULL DEFAULT ''
        );""",
            _kwargs={},
            _source="local_settings.db",
        )
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

        # TODO конвертируем и изменяем
        _temp_plan_high = int(_params.get("temp_plan_high", -7)) + 1
        _temp_plan_down = int(_params.get("temp_plan_down", -20)) + 1
        _data = {"temp_plan_high": _temp_plan_high, "temp_plan_down": _temp_plan_down}

        # TODO записываем в базу
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

    def push_button_temp_plan_minus(self):
        """
        * TODO берём старые
        * TODO конвертируем и изменяем
        * TODO записываем в базу
        """
        print(f"{datetime.datetime.now()} start pushButton_temp_plan_plus")

        # TODO берём старые
        Utils.sql_execute(
            _query="""
        CREATE TABLE IF NOT EXISTS params (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE NOT NULL,
            value TEXT NOT NULL DEFAULT ''
        );""",
            _kwargs={},
            _source="local_settings.db",
        )
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

        # TODO конвертируем и изменяем
        _temp_plan_high = int(_params.get("temp_plan_high", -7)) - 1
        _temp_plan_down = int(_params.get("temp_plan_down", -20)) - 1
        _data = {"temp_plan_high": _temp_plan_high, "temp_plan_down": _temp_plan_down}

        # TODO записываем в базу
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

    def update_ui_from_local_settings(self):
        """
        TODO Берём настройки c локальной базы данных
        TODO Устанавливаю настройки в интерфейс
        """
        # print(f"{datetime.datetime.now()} start update_ui_from_local_settings")

        # TODO Берём настройки c локальной базы данных ##################################################################
        Utils.sql_execute(
            _query="""
        CREATE TABLE IF NOT EXISTS params (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE NOT NULL,
            value TEXT NOT NULL DEFAULT ''
        );""",
            _kwargs={},
            _source="local_settings.db",
        )
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

        # TODO Устанавливаю настройки в интерфейс ##################################################################
        self.__params["temp_plan_high"] = int(_params.get("temp_plan_high", -7))
        self.__params["temp_plan_down"] = int(_params.get("temp_plan_down", -20))

        self.ui.label_temp_plan_high.setText(str(self.__params["temp_plan_high"]))
        self.ui.label_temp_plan_down.setText(str(self.__params["temp_plan_down"]))

    @staticmethod
    def update_settings_from_web():
        _headers = {"Authorization": "Token=auth123"}
        _response = requests.get("http://127.0.0.1:8008/api/settings/get/", headers=_headers)
        if _response.status_code not in (200, 201):
            raise Exception(f"WEB ERROR {_response.status_code}")
        _data = _response.json().get("data", {})
        Utils.sql_execute(
            _query="""
CREATE TABLE IF NOT EXISTS params (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE NOT NULL,
    value TEXT NOT NULL DEFAULT ''
);""",
            _kwargs={},
            _source="local_settings.db",
        )
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

    def loop(self):
        def loop_update_ui():
            while True:
                try:
                    threading.Thread(target=self.update_ui_from_local_settings, args=()).start()
                except Exception as error:
                    print(f"{datetime.datetime.now()} loop_update_ui:", error)
                time.sleep(0.2)

        def loop_update_settings_from_web():
            while True:
                try:
                    threading.Thread(target=self.update_settings_from_web, args=()).start()
                except Exception as error:
                    print(f"{datetime.datetime.now()} loop_update_settings_from_web:", error)
                time.sleep(5)

        threading.Thread(target=loop_update_ui, args=()).start()
        threading.Thread(target=loop_update_settings_from_web, args=()).start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui()
    sys.exit(app.exec())
