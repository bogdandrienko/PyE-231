from aiogram import Bot, Dispatcher, executor, types
import sqlite3

bot_instanse = Bot(token='6098525740:AAGQVVzGA3mE4qvhx-YUYFncz2FzEe-9jRk')
bot = Dispatcher(bot_instanse)


class DataBase:
    @staticmethod
    def execute_query_to_sqlite(query: str, args=(), many=True, silent_error=True) -> any:
        try:
            with sqlite3.connect('database.db') as connection:
                cursor = connection.cursor()
                cursor.execute(query, args)
                if many:
                    return cursor.fetchall()
                return cursor.fetchone()
        except Exception as error:
            print(error)
            if silent_error is False:
                raise Exception(error)
            return None

    @staticmethod
    def create_tovars_table():
        DataBase.execute_query_to_sqlite(query="""
CREATE TABLE IF NOT EXISTS tovars
(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
title TEXT, 
description TEXT, 
price INTEGER,
count INTEGER
)
""")

    @staticmethod
    def insert_tovar(title: str, description: str, price: int, count: int):
        DataBase.execute_query_to_sqlite(
            query="""
INSERT INTO tovars (title, description, price, count)
VALUES (?, ?, ?, ?)
""",
            args=(title, description, price, count))

    @staticmethod
    def get_all_tovars() -> list[tuple] | None:
        data = DataBase.execute_query_to_sqlite(
            query="""
SELECT id, title, description, price, count 
FROM tovars 
ORDER BY price DESC
""")
        return data


@bot.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("""
Привет!
Я почти ничего не умею!

Мои возможности:
/tovars - просмотр всех товаров
/tovar/1 - просмотр товара #1
    
""")


@bot.message_handler(commands=['tovars', 'tovar'])
async def get_tovars(message: types.Message):
    # берём из базы данных все товары
    tovars = DataBase.get_all_tovars()

    # создаём массив кнопок
    buttons = []
    for tovar in tovars:
        _button = types.KeyboardButton(text=f'#{tovar[0]} {tovar[1]} [{tovar[3]}] ({tovar[4]})')
        buttons.append(_button)
    keyboard = types.ReplyKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)

    # возвращаем в качестве ответа весь дизайн
    await message.reply("Выберите одну из кнопок:", reply_markup=keyboard)


# @bot.message_handler()
# async def echo(message: types.Message):
#     await message.answer(str(message.text)[::-1])


if __name__ == '__main__':
    """
1. Детальный просмотр выбранного товара
2. Добавление новых товаров в базу данных
    """

    # print(DataBase.get_all_tovars())
    # DataBase.insert_tovar(title="Ботинки", description="Ботинки Ботинки", price=12600, count=2)
    # print(DataBase.get_all_tovars())

    print("bot started...")
    executor.start_polling(bot, skip_updates=True)
    print("bot stopped...")
    pass
