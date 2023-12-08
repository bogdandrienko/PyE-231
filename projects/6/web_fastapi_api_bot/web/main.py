from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
import openpyxl
from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet
import io
import aiosqlite
import sqlite3

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/submit")
async def submit(request: Request):
    # form = await request.json()
    # input_text = form_data.get("input_text")
    # print(form)
    form_data = await request.form()
    file = form_data["addition"]
    f = await file.read()
    # print(type(await file.read()), await file.read())
    workbook: Workbook = openpyxl.load_workbook(filename=io.BytesIO(f), data_only=True)
    worksheet: Worksheet = workbook.active
    data = tuple(worksheet.iter_rows(min_row=2, max_row=worksheet.max_row, min_col=1, max_col=worksheet.max_column, values_only=True))
    print(data)
    clear_data = []
    for i in data:
        is_have_none = False
        for j in i:
            if j is None:
                is_have_none = True
        if not is_have_none:
            clear_data.append(i)
        # if all(j is not None for j in i):  # синтаксический сахар
        #     clear_data.append(i)
    print(clear_data)


    async with aiosqlite.connect('database.db') as db:
        await db.execute('''
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY UNIQUE NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    price REAL default 0.0,
    quantity INTEGER default 0
)''')
        await db.commit()

        # SQL Injection - уязвимость в БД
        # пришли данные, из файла, из input(html form)...
        # злоумышленник/вредитель мог вставит в поле вредоносный SQL код
#         await db.execute(f'''
# INSERT INTO my_table (id, name, description, price, quantity)
# VALUES ({data[0]}, 'Боты', 'Удобные боты', 70.5, 3)
# ''')
        it = clear_data[0]
        print(it)
        await db.execute('''
INSERT INTO items (id, name, description, price, quantity)
VALUES (:id, :name, :description, :price, :quantity)
''', {"id": it[0], "name": it[1], "description": it[2], "price": it[3], "quantity": it[4]})  # todo sql injection SAFE
        # placeholder - держатель места (ЗАГЛУШКА)
        await db.commit()

    # async with aiosqlite.connect('mydatabase.db') as db:
    #     # Выполняем SELECT-запрос
    #     cursor = await db.execute('SELECT * FROM items')
    #     rows = await cursor.fetchall()
    #     await cursor.close()
    #     return rows

    # async with aiohttp.ClientSession() as session:
    #     async with session.get("http://127.0.0.1:8003/api") as response:
    #         data = await response.json()
    # return {"data": data}

    return templates.TemplateResponse("index.html", {"request": request})
