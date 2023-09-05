########################################################################################################################
# TODO базы данных

import psycopg2

# CRUD

# Read - чтение(сортировка и фильтрация) из базы
# Create - вставка новых данных
# Delete - удаление строк (по условиям)
# Update - обновление из базы

connection = None
cursor = None

try:
    # connection = psycopg2.connect("dbname=example user=postgres password=12345Qwerty!")
    connection = psycopg2.connect(
        user="postgres",
        password="12345Qwerty!",
        host="127.0.0.1",  # 'localhost' \ '192.168.158.16'
        port="5432",
        dbname="example",
    )
    connection.autocommit = False
    cursor = connection.cursor()
    query_string1 = '''
DELETE FROM public.example_table
WHERE id = 888
    '''
    query_string2 = '''
SELECT * FROM public.example_table
WHERE age = 50
ORDER BY id ASC
    '''
    query_string3 = '''
CREATE TABLE public.table1
(
    title text NOT NULL,
    id serial NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.table1
    OWNER to postgres;
    '''
    query_string4 = f"""
INSERT INTO public.products (tovar, gruppa, postavshick, date_post, region, prodashi, sbit, pribil)
VALUES ('tovar', 'gruppa', 'postavshick', '2022-06-06', 'region', '500', '600', 'true')
"""
    cursor.execute(query_string1)
    records = cursor.fetchall()
    print(records, type(records))
    for i in records:
        print(i, type(i))
    connection.commit()
except Exception as error:
    print(error)
    connection.rollback()
finally:
    cursor.close()
    connection.close()

########################################################################################################################

########################################################################################################################
# TODO READ (SELECT)

# Connect to your postgres DB
conn = psycopg2.connect("dbname=example user=postgres password=31284bogdan")  # localhost (127.0.0.1 / 192.168.1.121)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query

# read data
cur.execute("""
SELECT * FROM public.example_table
WHERE age > 19
ORDER BY Age ASC, credits DESC
""")

# Retrieve query results
records = cur.fetchall()

print(records)
print(type(records))

for i in records:
    print(i)
    print(type(i))

conn.close()

########################################################################################################################

########################################################################################################################
# TODO CREATE (INSERT)

conn = psycopg2.connect("dbname=example user=postgres password=31284bogdan")
cur = conn.cursor()

# ('t', 25, True, 30000.6, 1)

new_arr = [
    ['w', 25, 'true', 30000.6, 1],
    ['b', 50, 'false', 30.6, 1],
    ['y', 25, 'true', 30000.6, 1],
    ['r', 75, 'false', 500.6, 0],
    ['u', 88, 'true', 30000.6, 1],
    ['3', 25, 'true', 305.6, 0],
]

# create data
index = 12
for i in new_arr:
    query_string = f"""
    INSERT INTO public.example_table (username, age, married, credits, id) 
    VALUES ('{i[0]}', {i[1]}, {i[2]}, {i[3]}, {index})
    """
    index += 1

    cur.execute(query_string)
    conn.commit()  # применение данных после изменений

conn.close()

########################################################################################################################

########################################################################################################################
# TODO DELETE (DELETE)

conn = psycopg2.connect("dbname=example user=postgres password=31284bogdan")
cur = conn.cursor()

query_string = """
    DELETE FROM public.example_table
    WHERE age <= 50 and married = 'true';
    """

#

cur.execute(query_string)
conn.commit()
conn.close()

########################################################################################################################

########################################################################################################################
# TODO UPDATE (UPDATE)

conn = psycopg2.connect("dbname=example user=postgres password=31284bogdan")
cur = conn.cursor()

query_string = """
UPDATE public.example_table
SET credits = '666.66' 
WHERE id = 2;
"""

#

cur.execute(query_string)
conn.commit()
conn.close()

########################################################################################################################

########################################################################################################################
# TODO CREATE TABLE

conn = psycopg2.connect("dbname=example user=postgres password=31284bogdan")
cur = conn.cursor()

query_string = """
CREATE TABLE public.products
(
    tovar text,
    gruppa text,
    postavshick text,
    date_post date,
    region text,
    prodashi integer DEFAULT 0,
    sbit integer DEFAULT 0,
    pribil boolean NOT NULL DEFAULT false,
    id SERIAL,
    PRIMARY KEY (id)
);
ALTER TABLE IF EXISTS public.products
    OWNER to postgres;
"""
cur.execute(query_string)
conn.commit()
conn.close()

########################################################################################################################

########################################################################################################################
# TODO test error

try:
    connection_string = "dbname='flask_database' user='flask_user' host='localhost' password='12345qwertY!'"
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    connection.autocommit = False
    cursor.execute("""INSERT INTO zarplata (username, salary) VALUES ('Bogdan', '60000'), ('Alice', '80000');""")
    cursor.execute("""select * from zarplata;""")
    # print(10 - "")  #
    # print({"name": "Bogdan"}["username"])  #
    data = cursor.fetchall()
    print(data)
    print(len(data))
    print(10 / 0)  # ZEROdivision
except Exception as error:
    connection.rollback()
    print(error)
else:
    connection.commit()
finally:
    cursor.close()
    connection.close()

########################################################################################################################

########################################################################################################################
# TODO pyodbc library

import pyodbc

ip = ""
server = ""
port = ""
database = ""
username = ""
password = ""
conn_str = (
        r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=tcp:' + ip + '\\' + server + ',' + port +
        ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password + ';'
)
conn = pyodbc.connect(conn_str)

table = ""

cursor = connection.cursor()
cursor.fast_executemany = True
__rows = ''
# for x in rows:
#     __rows = f"{__rows}{str(x)}, "
# value = f"UPDATE {table} SET {rows[1]} = '{values[1]}',{rows[2]} = '{values[2]}' ,{rows[3]} = '{values[3]}' " \
#         f"WHERE {rows[0]} = '{values[0]}'"
# cursor.execute(value)
connection.commit()

########################################################################################################################
