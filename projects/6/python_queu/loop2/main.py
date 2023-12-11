import time
import sqlite3

# MVP - быстрый код
while True:
    time.sleep(2.0)

    # TODO чтение из базы данных
    with sqlite3.connect("../sqlite3.db") as connection:  # контекстный менеджер(освобождает ресурсы)
        cursor = connection.cursor()
        cursor.execute(
            """
    CREATE TABLE IF NOT EXISTS items (
        id integer primary key autoincrement not null,
        name TEXT,
        price INTEGER
    )
    """
        )
        connection.commit()
        # TODO чтение последней задачи
        cursor.execute("SELECT id, name, price from items order by id DESC limit 1")
        row = cursor.fetchone()
        if not row:
            print("pass")
            continue
        print(row)

        # TODO дозапись последнего элемента
        with open("../results.txt", "a", encoding="utf-8") as f:
            f.write(f"{row[1]} {row[2]}\n")

        # TODO удаляет успешно отправленную задачу
        cursor.execute("DELETE from items where id = :_id", {"_id": row[0]})
        # cursor.execute("DELETE from items where id = '?'", (row[0],))
        connection.commit()
