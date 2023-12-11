import time
import sqlite3

# pip install pyinstaller
# pyinstaller --onefile --console main.py

# MVP - быстрый код
while True:
    time.sleep(1.0)

    # TODO чтение исходного
    with open("../source.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        # print(lines)
        if not lines:
            print("pass")
            continue
        # TODO цель
        last_line = str(lines[-1]).strip()  # " Me   \t"
        print(last_line)
        new_lines = lines[:-1]  # slice - срез
        # print(new_lines)

    # TODO запись в базу данных
    # Подключение к базе данных (если базы данных нет, она будет создана)
    conn = sqlite3.connect("../sqlite3.db")
    # Создание курсора
    cursor = conn.cursor()
    # Создание таблицы, если её ещё нет
    cursor.execute(
        """
CREATE TABLE IF NOT EXISTS items (
    id integer primary key autoincrement not null,
    name TEXT,
    price INTEGER
)
"""
    )
    # Пример данных
    name = str(" ".join(last_line.split(" ")[0:-1])).strip()
    price = int(str(last_line.split(" ")[-1]).strip())  # последнее слово - цена
    # Вставка данных в таблицу
    cursor.execute("INSERT INTO items (name, price) VALUES (?, ?)", (name, price))
    # Подтверждение изменений
    conn.commit()
    # Закрытие соединения с базой данных
    conn.close()

    # TODO перезапись без последнего элемента
    with open("../source.txt", "w", encoding="utf-8") as f:
        f.writelines(new_lines)
