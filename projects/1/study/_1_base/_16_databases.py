########################################################################################################################
# TODO базы данных

import psycopg2  # PostgreSQL
import sqlite3


# pyodbc - MSSQL / MySQL
# cx_oracle - Oracle
# mysqlconnector MySQL....
# sqlite3 SQLITE


# 1. В мире много данных! Даже в рамках одного проекта, данных много!
# 2. Эти данные, даже если структурированы, всё равно их нужно быстро "отдавать", "вставлять"... CRUD
# 3. Самая популярная база данных для python и web - PostgreSQL. Желательно не использовать интерфейс.

# логически структурированные - SQL - реляционные - отношение/связь
# СУБД — комплекс программ, позволяющих создать базу данных и манипулировать данными
# (вставлять, обновлять, удалять и выбирать).

# MySQL, PostgreSQL, Oracle, MSSQL, sqlite (встраиваемая)
# 95% - похожи

# логически не структурированные - NOSQL -
# иерархические, ключ-значение(Redis), графы, документы, big data - MongoDB

# CRUD
# Create    | INSERT
# Read      | SELECT
# Update    | UPDATE
# Delete    | DELETE

# https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
# https://dev.mysql.com/downloads/file/?id=518835

# id                            name            price               is_view     count   description     datetime
# int                           str             Decimal             bool        int    str             datetime.date
# (serial / autoincrement)      varchar(200)    double precision   boolean   bigint     varchar(2000)   date

# 1. В реальности - сервер это всегда консоль, нет интерфейса.
# 2. Чистый SQL - более гибкий.
# 3. Проще автоматизировать.

def query(query_str: str, args: tuple, many=True) -> list | None:
    with psycopg2.connect(dbname="market_place", host="127.0.0.1", user="postgres", password="31284bogdan", port="5432") as connection:
        with connection.cursor() as cursor:
            cursor.execute(query_str, args)
            try:
                if many:
                    return cursor.fetchall()  # list[tuple[any]]
                return cursor.fetchone()  # tuple[any]
            except Exception as error:
                return None


def query_old(query_str: str) -> list | None:
    connection = None
    cursor = None
    rows = None

    try:
        connection = psycopg2.connect(dbname="market_place", host="localhost", user="postgres", password="31284bogdan", port="5432")
        cursor = connection.cursor()
        query_create_table = """
    SELECT id, title FROM public.posts
    ORDER BY title DESC
    """
        cursor.execute(query_str)
        rows = cursor.fetchall()
    except Exception as error:
        print("error: ", error)
    finally:
        cursor.close()
        connection.close()
        return rows


def query_with_injection() -> list | None:
    text_ = "Нужно помыть кота!;create user natalia with password admin;get all privilegies;"
    query_str = f"INSERT INTO posts (title) VALUES ('{text_}')"
    with psycopg2.connect(dbname="market_place", host="127.0.0.1", user="postgres", password="31284bogdan", port="5432") as connection:
        with connection.cursor() as cursor:
            cursor.execute(query_str)
            try:
                return cursor.fetchall()
            except Exception as error:
                return None


def query_without_injection() -> list | None:
    text_ = "Нужно помыть кота!;create user natalia with password admin;get all privilegies;"
    query_str = f"INSERT INTO posts (title, decrtiption) VALUES ('%s', '%s')"  # postgres - %s | sqlite - ?
    with psycopg2.connect(dbname="market_place", host="127.0.0.1", user="postgres", password="31284bogdan", port="5432") as connection:
        with connection.cursor() as cursor:
            cursor.execute(query_str, (text_, 123))
            try:
                return cursor.fetchall()
            except Exception as error:
                return None


def queries():
    """"""

    """
    SELECT * FROM public.products;
    """  # выборка ВСЕХ данных и всех полей с таблицы

    """
    SELECT id, name, price FROM public.products;
    """  # выборка ВСЕХ данных, но только указанных полей

    """
    SELECT * FROM public.products 
    ORDER BY price DESC;
    """  # выборка ВСЕХ данных, но с сортировкой по цене по убыванию

    """
    SELECT * FROM public.products
    WHERE id = 1;
    """  # выборка ТОЛЬКО строки, где id = 1 данных

    """
    SELECT * FROM public.products
    /*WHERE price > 300*/
    -- where
    WHERE price < 2000 AND is_view = 'true';
    """  # выборка ТОЛЬКО строки, где id = 1 данных

    """
    INSERT INTO public.products (name, price, count, is_view, description) 
    VALUES ('Груши', '1200.5', '4', 'true', 'я груша');
    """  # вставка(создание) 1 новой строки

    """
    INSERT INTO public.products (name, price, count, is_view, description) 
    VALUES ('Груши 1', '1200.5', '4', 'true', 'я груша'), 
            ('Груши 2', '1200.5', '4', 'true', 'я груша'), 
            ('Груши 3', '1200.5', '4', 'true', 'я груша');
    """  # вставка(создание) новых строк

    """
    DELETE FROM public.products
    WHERE count='4';
    """  # удаление строк по условию

    """
    UPDATE public.products 
    SET count = count + 2 
    WHERE description = 'красная';
    """  # обновление выбранных полей по условию


if __name__ == "__main__":
    print(query("SELECT * FROM posts"))
    # print(query("INSERT INTO posts (title) VALUES ('Макароны')"))

    # todo SQL injection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    text = "Нужно помыть кота!;drop table postgres;"
    text = "Нужно помыть кота!;create user natalia with password admin;get all privilegies;"
    # text = input("Что вы хотите?")
    print(query(f"INSERT INTO posts (title) VALUES ('{text}')", (text, )))
    # todo SQL injection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # print(query("DELETE FROM posts WHERE title='Салат';"))
    print(query("SELECT * FROM posts"))

