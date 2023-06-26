import threading
import time

from PyQt6.QtCore import QRect
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QCheckBox, QTextEdit
import sys
import datetime
import sqlite3


# pyqt - высокопроизводительный, стандарт индустрии
# tkinter - встроенный, лёгкий

def query(query_str: str, args=(), many=True) -> list | None:
    with sqlite3.connect('database/database.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query_str, args)
        try:
            if many:
                return cursor.fetchall()
            return cursor.fetchone()
        except Exception as error:
            return None


def create_db() -> None:
    query_str = '''
CREATE TABLE IF NOT EXISTS notes
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
status TEXT,
datetime TEXT
);
'''
    query(query_str)


def insert_db(title: str, status=False, date_time=None) -> None:
    if date_time is None:
        date_time = datetime.datetime.now()
    query_str = '''
INSERT INTO notes (title, status, datetime)
VALUES (?, ?, ?);
'''
    query(query_str, (title, int(status), date_time))


def select_db() -> list[tuple[any]] | None:
    query_str = '''
SELECT id, title, status, datetime FROM notes
ORDER BY id DESC;
'''
    rows_raw = query(query_str, many=True)
    return rows_raw


def delete_db() -> None:
    query_str = '''
DELETE FROM notes;
'''
    query(query_str)


def test_db():
    # create_db()
    # insert_db("Купить слона")
    print(select_db())
    # insert_db("Купить слона")
    print(select_db())


def get_data_ph():
    # TODO - как в другом потоке обновлять объект
    # thread = threading.Thread(target=get_data, args=(), kwargs={})
    # thread.start()
    pass


def get_data():
    time.sleep(1.0)

    rows_raw = select_db()
    # print(rows_raw)
    data_str = ""
    for row in rows_raw:
        data_str += f'#{row[0]} {row[1]} ({"Выполнено" if int(row[2]) == 1 else "Не выполнено"}) [{row[3]}]'
    # print(data_str)
    # [
    # (4, 'Купить кота', '0', '2023-06-26 21:01:57.061831'),
    # (3, 'Купить верблюда', '1', '2023-06-26 21:00:52.221044'),
    # (2, '1111111111111111111111', '1', '2023-06-26 20:59:41.901095'),
    # (1, 'Купить слона', '0', '2023-06-26 20:22:13.896782')
    # ]

    # 0.1
    return data_str


def send_data():
    text = str(edit_title.text())
    status = bool(check_box.isChecked())
    # print(select_db())
    insert_db(title=text, status=status)
    # print(select_db())

    edit_title.setText("")
    check_box.setChecked(False)

    text_data.setText(get_data())


def reset_data():
    delete_db()

    text_data.setText(get_data())


if __name__ == "__main__":
    # Приложение для публикации "заметок" и их вывода на экран

    # Практика: сохранение данных в базу данных и чтение данных из файла (excel - export/import)
    # Система экспорта-импорта, конвертация.
    # text_edit - путь к файлу(имя файла)
    # две кнопки - импортировать - берёт данные из указанного excel файла(наименование, количество, цена)
    #           - экспортировать - берёт данные из базы данных (id, наименование, количество, цена) и записывает в новый excel файл

    # https://build-system.fman.io/qt-designer-download
    # https://habr.com/ru/companies/skillfactory/articles/599599/
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Название окна")
    window.setGeometry(QRect(200, 200, 640, 480))
    window.setMinimumSize(640, 480)
    window.setMaximumSize(3840, 2160)

    grid = QGridLayout()
    grid.setSpacing(10)

    label_title = QLabel('Наименование задачи')
    grid.addWidget(label_title, 0, 0)

    text_data = QTextEdit(get_data())
    grid.addWidget(text_data, 3, 3)

    edit_title = QLineEdit()
    grid.addWidget(edit_title, 0, 1)

    label_check = QLabel('Статус задачи')
    grid.addWidget(label_check, 0, 2)

    check_box = QCheckBox()
    grid.addWidget(check_box, 0, 3)

    button_start = QPushButton('сохранить')
    button_start.clicked.connect(send_data)
    grid.addWidget(button_start, 1, 1)

    button_reset = QPushButton('сбросить')
    button_reset.clicked.connect(reset_data)
    grid.addWidget(button_reset, 2, 1)

    window.setLayout(grid)

    window.show()
    app.exec()
    pass
