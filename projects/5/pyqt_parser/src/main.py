import asyncio
import json
import time
import concurrent.futures
import aiohttp
from bs4 import BeautifulSoup


class Valute:
    def __init__(self, name: str, symbol: str, priceUSD: float):
        self.name = str(name)
        self.symbol = str(symbol)
        self.priceUSD = float(priceUSD[1:].replace(',', ''))

    def __repr__(self):
        return f"<Valute {self.name} {self.symbol} {self.priceUSD}>"

    def to_json(self) -> str:
        return json.dumps({"name": self.name, "symbol": self.symbol, "price": self.priceUSD, "active": True})


class View:
    @staticmethod
    def calculate_o(mat: list[any]) -> Valute:
        val = Valute(name=mat[1], symbol=mat[2], priceUSD=mat[3])
        # print(val)
        time.sleep(2.0)  # НАГРУЗКА
        return val

    @staticmethod
    def calculate_m(matrix: list[list[any]], workers: int = (8 * 2 + 1) * 2) -> list[Valute]:
        """
        В не более чем 100 потоках.
        """

        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            futures = []
            for i in matrix:
                futures.append(executor.submit(View.calculate_o, i))
            results = []
            for future in concurrent.futures.as_completed(futures):
                results.append(future.result())
        return results


async def async_request(url: str, headers: dict) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as response:
            data = await response.read()
            return data.decode()


async def get_valutes(url: str, filter_by_price: float) -> list[Valute]:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }

    # получение ответа в формате str
    response = await async_request(url=url, headers=headers)
    # парсинг ответа в объект BeautifulSoup
    soup = BeautifulSoup(response, 'html.parser')
    # поиск всех тэгов "tbody", взятие первого
    tbody = soup.find_all('tbody')[0]
    # разделение всего текста на блоки
    lines = tbody.text.split("\n")
    # фильтрация (отбрасывает все "пустые строки")
    lines = list(filter(lambda x: str(x).strip() != "", lines))

    elems = []  # чужая песочница
    local_elems = []  # ведёрко
    index = 0  # количество лопаток(счётчик)
    for i in lines:  # наша песочница
        # опускаем лопатку с песком в ведёрко
        local_elems.append(i)
        index += 1
        # проверям наполнено ли ведёрко
        if index >= 11:
            # тащим ведёрко в чужую песочницу
            elems.append(local_elems)
            # обнуляем ведёрко
            local_elems = []
            index = 0

    vals: list[Valute] = View.calculate_m(matrix=elems)
    vals = list(filter(lambda x: x.priceUSD > filter_by_price, vals))
    vals = sorted(vals, key=lambda x: (x.priceUSD, x.name), reverse=True)
    for i in vals:
        print(i.to_json())


if __name__ == "__main__":
    """
    MVP
    1. Проверит, что интерфейс на целевых платформах работает
    """
    asyncio.run(get_valutes(url="https://www.coingecko.com/", filter_by_price=1000.0))
