import psycopg2


def teory():
    """
    Todo List: блокнот для ежедневных задач

    * Записывать(добавлять) новые задачи (помыть кота)
    * Читать задачи из файла/базы данных(только базы
    данных могут обеспечить высокую производительность)
    * Изменять(обновлять)
    * Удалять

    * CRUD
    * Create (INSERT)
    * Read (SELECT)
    * Update (UPDATE)
    * Delete (DELETE)



    Релятивные(SQL - 95% родственны) - формализованные и строгие (excel)
    MySQL - 35%, best for PHP
    PostgreSQL - 25%, best for Python
    Oracle - 25%, best for Business(надёжность)   $
    MSSQL - 10%                                   $
    SQLite - ??%, best for mobile(встраиваемая - локальная - просто файл) - смартфоны
    ...

    СУБД - система управления базами данных
    https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

    Не релятивные(NO SQL)
    MongoDB - (json, 10 000 000 000)
    Redis - key-value (огромный словарь)



    СУБД[FOLDER] -> magazine(database)[WORKBOOK] -> news(table)[WORKSHEET] ->
    (id: serial(1, 2, 3...), title: var(VARCHAR), description: var(VARCHAR),
    price: double precision, is_actual: bool, datatime: time_stamp)[COLUMNS]





    """

    query = """
    
    -- СОЗДАНИЕ ТАБЛИЦЫ ДАННЫХ
    CREATE TABLE public.news
    (
        id serial NOT NULL,
        title character varying(250),
        description character varying(2000) DEFAULT '',
        price double precision NOT NULL DEFAULT 0.0,
        is_actual boolean NOT NULL DEFAULT false,
        datatime timestamp without time zone DEFAULT NOW(),
        PRIMARY KEY (id)
    );
    ALTER TABLE IF EXISTS public.news
        OWNER to postgres;
        
        
        
        
    -- Выборка всех данных
    
    SELECT * FROM news;
    
    /*
    SELECT id, title, price from news -- время, экономия памяти, экономия трафика
    WHERE price >= 300 -- фильтрация(условия)
    ORDER BY PRICE ASC; -- сортировка
    */
    
    /*
    SELECT title, SUM(price) / 3 price from news
    GROUP BY TITLE -- группировка
    ORDER BY PRICE DESC;
    */
    
    -- вставка
    INSERT INTO public.news (title, description, price, is_actual)
    VALUES ('Апокалипсис', 'Апокалипсис описание', '3500.5', 'true');
        
    -- обновление
    UPDATE public.news
    SET price = price * 1.5
    WHERE id > 4 ;
    
    -- удаление
    DELETE FROM public.news
    WHERE is_actual = 'true'
        
    """


connection = psycopg2.connect(
    user="postgres",  # TODO DANGER
    password="31284bogdan",  # TODO DANGER
    host="127.0.0.1",  # 'localhost' \ '192.168.158.16'  # IP ADDRESS
    port="5432",  # HOST+PORT = SOCKET
    dbname="magazine",
)
connection.autocommit = False
cursor = connection.cursor()


def select():
    query1 = """
SELECT * FROM news;
"""
    cursor.execute(query1)
    rows: list[tuple[any]] = cursor.fetchall()  # fetchall = [()]  | fetchone = ()
    # print(rows)
    for r in rows:
        print(r)


def insert():
    query2 = """
INSERT INTO public.news (title, description, price, is_actual)
VALUES ('Праздник', 'Конец занятия', '8000', 'false');
"""
    cursor.execute(query2)
    connection.commit()
