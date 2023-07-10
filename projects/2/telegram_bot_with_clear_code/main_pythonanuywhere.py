"""Наш телеграм бот"""

import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message

#

PROXY_URL = "http://proxy.server:3128"
bot = Bot(token="6098525740:AAGQVVzGA3mE4qvhx-YUYFncz2FzEe-9jRk", proxy=PROXY_URL)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class DataBase:
    """Класс для работы с базой данных"""

    @staticmethod
    def execute_query_to_sqlite(
            query: str, args: tuple, many: False, silent_error=True
    ) -> any:
        """Выполняет запрос к базе данных и возвращает результат"""

        try:
            with sqlite3.connect("database.db") as connection:
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
        """Создает таблицу товаров в базе данных"""

        DataBase.execute_query_to_sqlite(
            query="""
CREATE TABLE IF NOT EXISTS tovars
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
description TEXT,
price INTEGER,
count INTEGER
)
""",
            args=(),
            many=True,
        )

    @staticmethod
    def insert_tovar(title: str, description: str, price: int, count: int):
        """Добавляет товар в базу данных"""

        DataBase.execute_query_to_sqlite(
            query="""
INSERT INTO tovars (title, description, price, count)
VALUES (?, ?, ?, ?)
""",
            args=(title, description, price, count),
            many=True,
        )

    @staticmethod
    def get_one_tovar(_id: int) -> tuple | None:
        """Берёт один товаров из базы данных по id"""

        return DataBase.execute_query_to_sqlite(
            query="""
SELECT id, title, description, price, count
FROM tovars
WHERE id = ?
""",
            args=(_id,),
            many=False,
        )

    @staticmethod
    def get_all_tovars() -> list[tuple] | None:
        """Берёт все товары из базы данных"""

        return DataBase.execute_query_to_sqlite(
            query="""
SELECT id, title, description, price, count
FROM tovars
ORDER BY price DESC
""",
            args=(),
            many=True,
        )


class Register(StatesGroup):
    """Машина состояний - переключатель между функциями"""

    title = State()
    description = State()
    price = State()
    count = State()


@dp.message_handler(commands=["start", "help"])
async def f_start(message: types.Message):
    """start"""

    await message.reply(
        """
Привет!
Я почти ничего не умею!

Мои возможности:
/tovars - просмотр всех товаров
/create - публикацию своего товара
    
"""
    )


@dp.message_handler(commands=["tovars"])
async def f_tovars(message: types.Message):
    """Получает список всех товаров из базы данных"""

    # берём из базы данных все товары
    _tovars = DataBase.get_all_tovars()

    # создаём массив кнопок
    _buttons = []
    for _tovar in _tovars:
        _button = types.InlineKeyboardButton(
            text=f"#{_tovar[0]} {_tovar[1]} [{_tovar[3]}] ({_tovar[4]})",
            callback_data=f"get_tovar|{_tovar[0]}",
        )
        _buttons.append(_button)
    _keyboard = types.InlineKeyboardMarkup(row_width=3)
    _keyboard.add(*_buttons)

    # возвращаем в качестве ответа весь дизайн
    await message.reply("Выберите одну из кнопок:", reply_markup=_keyboard)


@dp.message_handler(commands=["create"])
async def f_create(message: types.Message):
    """Выводит кнопку для создания карточки"""

    _button = types.InlineKeyboardButton(
        text="Опубликуйте свой товар!",
        callback_data="public",
    )
    _keyboard = types.InlineKeyboardMarkup(row_width=2)
    _keyboard.add(_button)

    await message.reply(
        "Нажмите, чтобы <u>создать карточку</u>:",
        reply_markup=_keyboard,
        parse_mode="HTML",
    )


@dp.message_handler(state=Register.title)
async def create_title(message: Message, state: FSMContext):
    """Ввод наименования товара"""

    await state.update_data(title=str(message.text).strip())
    await message.reply("Введите, <u>описание</u> товара: ❗️", parse_mode="HTML")
    await Register.description.set()


@dp.message_handler(state=Register.description)
async def create_description(message: Message, state: FSMContext):
    """Ввод наименования товара"""

    await state.update_data(description=str(message.text).strip())
    await message.reply("Введите, <u>цену</u> товара: ❗️", parse_mode="HTML")
    await Register.price.set()


@dp.message_handler(state=Register.price)
async def create_price(message: Message, state: FSMContext):
    """Ввод цены товара"""

    await state.update_data(price=str(message.text).strip())
    await message.reply("Введите, <u>количество</u> товара: ❗️", parse_mode="HTML")
    await Register.count.set()


@dp.message_handler(state=Register.count)
async def create_count(message: Message, state: FSMContext):
    """Ввод количества товара"""

    await state.update_data(count=str(message.text).strip())
    user_data = await state.get_data()
    try:
        DataBase.insert_tovar(
            title=user_data["title"],
            description=user_data.get("description", ""),
            price=int(user_data["price"]),
            count=int(user_data["count"])
        )
        await message.reply("Товар <b>успешно</b> записан в базу данных!️", parse_mode="HTML")
    except Exception as error:
        await message.reply(f"Товар <b>не  записан</b> в базу данных!️({error})", parse_mode="HTML")
    await state.finish()


@dp.callback_query_handler(lambda callback_query: True)
async def handle_button_click(callback_query: types.CallbackQuery):
    """Обработка нажатия кнопки"""
    query_data = callback_query.data.split("|")[0]

    if query_data == "get_tovar":
        _args = callback_query.data.split("|")[1:]
        _pk = int(_args[0])
        detail = DataBase.get_one_tovar(_id=_pk)

        _button = types.InlineKeyboardButton(
            text="В корзину",
            callback_data=f"buy|{_pk}",
        )
        _keyboard = types.InlineKeyboardMarkup(row_width=3)
        _keyboard.add(_button)
        _text = f"""Карточка товара: \t\n
Наименование: {detail[1]}
Описание: {detail[2]}
Стоимость(количество): {detail[3]} ({detail[4]})
"""

        await callback_query.message.reply(_text, reply_markup=_keyboard)
        # await callback_quer
        # answer(text=f"Button clicked! {detail[2]}")  # всплывающее сообщение
    elif query_data == "buy":
        pass
    elif query_data == "public":
        await callback_query.message.reply(
            "Введите, <u>название</u> товара: ❗️", parse_mode="HTML"
        )
        await Register.title.set()
    else:
        pass


if __name__ == "__main__":
    _ = """
    1. Детальный просмотр выбранного товара
    2. Добавление новых товаров в базу данных
    """

    # print(DataBase.get_all_tovars())
    # DataBase.insert_tovar(title="Ботинки", description="Ботинки Ботинки", price=12600, count=2)
    # print(DataBase.get_all_tovars())

    print("bot started...")
    executor.start_polling(dp, skip_updates=True)
    print("bot stopped...")
