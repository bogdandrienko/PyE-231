from PyQt6.QtCore import QRect
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout
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


def test_db():
    # create_db()
    # insert_db("Купить слона")
    print(select_db())
    insert_db("Купить слона")
    print(select_db())


if __name__ == "__main__":
    # Приложение для публикации "заметок" и их вывода на экран
    # Практика: сохранение данных в базу данных и чтение данных из файла (excel - export/import)

    # https://build-system.fman.io/qt-designer-download
    # https://habr.com/ru/companies/skillfactory/articles/599599/
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Название окна")
    window.setGeometry(QRect(200, 200, 1280, 720))
    window.setMinimumSize(640, 480)
    window.setMaximumSize(3840, 2160)

    title = QLabel('Title')
    author = QLabel('Author')
    review = QLabel('Review')

    titleEdit = QLineEdit()
    authorEdit = QLineEdit()
    reviewEdit = QTextEdit()

    grid = QGridLayout()
    grid.setSpacing(10)

    grid.addWidget(title, 1, 0)
    grid.addWidget(titleEdit, 1, 1)

    grid.addWidget(author, 2, 0)
    grid.addWidget(authorEdit, 2, 1)

    grid.addWidget(review, 3, 0)
    grid.addWidget(reviewEdit, 3, 1, 5, 1)

    window.setLayout(grid)

    window.show()
    app.exec()

    pass
